from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Product, Service, Reservation, Gallery
from account_module.models import User, PhoneOTP
from .serializer import (
    ReservationSerializer,
    ServiceSerializer,
    GallerySerializer,
    ProductSerializer,
    OtpVerifySerializer,
    PhoneSerializer
)
import random
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from rest_framework.viewsets import ModelViewSet, ViewSet


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post", "get"]


class RegisterViewSet(ViewSet):

    def create(self, request):
        serializer = PhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]

        if User.objects.filter(phone=phone).exists():
            return Response(
                {"detail": "این شماره قبلاً ثبت شده"},
                status=status.HTTP_400_BAD_REQUEST
            )

        code = str(random.randint(10000, 99999))
        PhoneOTP.objects.create(phone=phone, code=code)

        print("REGISTER OTP:", code)

        return Response({"detail": "کد ارسال شد"})


class VerifyRegisterViewSet(ViewSet):

    def create(self, request):
        serializer = OtpVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]

        otp = PhoneOTP.objects.filter(phone=phone, code=code).last()
        if not otp:
            return Response(
                {"detail": "کد نامعتبر است"},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(phone=phone)
        otp.delete()

        return Response({"detail": "ثبت‌نام موفق"})


class LoginViewSet(ViewSet):

    def create(self, request):
        serializer = PhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]

        if not User.objects.filter(phone=phone).exists():
            return Response(
                {"detail": "کاربر یافت نشد"},
                status=status.HTTP_404_NOT_FOUND
            )

        code = str(random.randint(10000, 99999))
        PhoneOTP.objects.create(phone=phone, code=code)

        print("LOGIN OTP:", code)

        return Response({"detail": "کد ورود ارسال شد"})


class VerifyLoginViewSet(ViewSet):

    def create(self, request):
        serializer = OtpVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]

        otp = PhoneOTP.objects.filter(phone=phone, code=code).last()
        if not otp:
            return Response(
                {"detail": "کد اشتباه است"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(phone=phone)
        login(request, user)

        otp.delete()

        return Response({"detail": "ورود موفق"})

# class SearchViewSet(ViewSet):
