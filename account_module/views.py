import random
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.utils import timezone
from .models import User, PhoneOTP
import re


def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")

        phone_pattern = r'^(09\d{9}|00989\d{9}|\+989\d{9})$'

        if not full_name or not phone:
            messages.error(request, "همه فیلدها الزامی است")
            return redirect("register_page")

        if not re.match(phone_pattern, phone):
            messages.error(request, "شماره موبایل معتبر نیست")
            return redirect("register_page")

        if User.objects.filter(phone=phone).exists():
            messages.error(request, "این شماره قبلاً ثبت شده")
            return redirect("login_page")

        if PhoneOTP.objects.filter(
                phone=phone,
                created_at__gte=timezone.now() - timedelta(minutes=1)
        ).exists():
            messages.error(request, "لطفاً کمی صبر کنید")
            return redirect("register_page")

        code = str(random.randint(10000, 99999))
        PhoneOTP.objects.create(phone=phone, code=code)

        print("REGISTER OTP:", code)

        request.session["register_phone"] = phone
        request.session["register_name"] = full_name

        return redirect("register_verify")

    return render(request, "account_module/register_page.html")


def register_verify_view(request):
    phone = request.session.get("register_phone")
    full_name = request.session.get("register_name")

    if not phone:
        return redirect("register_page")

    if request.method == "POST":
        code = request.POST.get("code")

        otp = PhoneOTP.objects.filter(
            phone=phone,
            code=code,
            created_at__gte=timezone.now() - timedelta(minutes=2)
        ).last()

        if not otp:
            messages.error(request, "کد نامعتبر یا منقضی شده")
            return redirect("register_verify")

        User.objects.create_user(phone=phone, full_name=full_name)
        otp.delete()

        request.session.pop("register_phone")
        request.session.pop("register_name")

        return redirect("register_success")

    return render(request, "account_module/register_verify.html")


def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")

        phone_pattern = r'^(09\d{9}|00989\d{9}|\+989\d{9})$'

        if not phone:
            messages.error(request, "شماره موبایل را وارد کنید")
            return redirect("login_page")

        if not re.match(phone_pattern, phone):
            messages.error(request, "شماره موبایل معتبر نیست")
            return redirect("login_page")

        if not User.objects.filter(phone=phone).exists():
            messages.error(request, "کاربری با این شماره یافت نشد")
            return redirect("login_page")

        if PhoneOTP.objects.filter(
                phone=phone,
                created_at__gte=timezone.now() - timedelta(minutes=1)
        ).exists():
            messages.error(request, "لطفاً کمی صبر کنید")
            return redirect("login_page")

        code = str(random.randint(10000, 99999))
        PhoneOTP.objects.create(phone=phone, code=code)

        print("LOGIN OTP:", code)

        request.session["login_phone"] = phone
        return redirect("login_verify")

    return render(request, "account_module/login_page.html")


def login_verify_view(request):
    phone = request.session.get("login_phone")

    if not phone:
        messages.error(request, "ابتدا شماره تلفن را وارد کنید")
        return redirect("login_page")

    if request.method == "POST":
        code = request.POST.get("code")

        otp = PhoneOTP.objects.filter(
            phone=phone,
            code=code,
            created_at__gte=timezone.now() - timedelta(minutes=2)
        ).last()

        if not otp:
            messages.error(request, "کد وارد شده اشتباه یا منقضی شده است")
            return redirect("login_verify")

        user = User.objects.get(phone=phone)
        login(request, user)

        otp.delete()
        request.session.pop("login_phone", None)  # ✅ امن

        return redirect("login_success")

    return render(request, "account_module/login_verify.html")


def register_success_view(request):
    return render(request, "account_module/register_success.html")


def login_success_view(request):
    return render(request, "account_module/login_success.html")

def logout_view(request):
    logout(request)
    return redirect("home_page")