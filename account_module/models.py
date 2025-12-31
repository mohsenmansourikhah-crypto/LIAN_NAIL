from django.db import models
from django.utils import timezone
import random
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import timedelta


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("شماره موبایل الزامی است")

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "phone"



class PhoneOTP(models.Model):
    phone = models.CharField(max_length=15, db_index=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.code}"

    @staticmethod
    def generate_code():
        return str(random.randint(10000, 99999))

    @staticmethod
    def is_valid(phone, code, minutes=2):
        return PhoneOTP.objects.filter(
            phone=phone,
            code=code,
            created_at__gte=timezone.now() - timedelta(minutes=minutes)
        ).exists()

    @staticmethod
    def can_send(phone, seconds=60):
        return not PhoneOTP.objects.filter(
            phone=phone,
            created_at__gte=timezone.now() - timedelta(seconds=seconds)
        ).exists()

    @staticmethod
    def cleanup(minutes=5):
        PhoneOTP.objects.filter(
            created_at__lt=timezone.now() - timedelta(minutes=minutes)
        ).delete()
