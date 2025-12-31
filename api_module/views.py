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
from rest_framework.decorators import api_view


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

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


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

        if not PhoneOTP.can_send(phone):
            return Response(
                {"detail": "لطفاً کمی بعد دوباره تلاش کنید"},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        PhoneOTP.cleanup()

        code = PhoneOTP.generate_code()
        PhoneOTP.objects.create(phone=phone, code=code)

        print("REGISTER OTP:", code)  # 👈 تست لوکال

        return Response({"detail": "کد ارسال شد"})



class VerifyRegisterViewSet(ViewSet):

    def create(self, request):
        serializer = OtpVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]

        if not PhoneOTP.is_valid(phone, code):
            return Response(
                {"detail": "کد نامعتبر یا منقضی شده است"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(phone=phone)

        PhoneOTP.objects.filter(phone=phone).delete()

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

        if not PhoneOTP.can_send(phone):
            return Response(
                {"detail": "لطفاً کمی بعد دوباره تلاش کنید"},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        PhoneOTP.cleanup()

        code = PhoneOTP.generate_code()
        PhoneOTP.objects.create(phone=phone, code=code)

        print("LOGIN OTP:", code)

        return Response({"detail": "کد ورود ارسال شد"})



class VerifyLoginViewSet(ViewSet):

    def create(self, request):
        serializer = OtpVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]

        if not PhoneOTP.is_valid(phone, code):
            return Response(
                {"detail": "کد اشتباه یا منقضی شده است"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(phone=phone)
        login(request, user)

        PhoneOTP.objects.filter(phone=phone).delete()

        return Response({"detail": "ورود موفق"})



# class SearchViewSet(ViewSet):


@api_view(['GET'])
def reserved_times(request):
    date = request.GET.get('date')
    times = Reservation.objects.filter(date=date).values_list('time', flat=True)
    return Response(list(times))
