from django.db import models
from django.utils import timezone
import random
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=20, unique=True)
    email_active_code = models.CharField(max_length=150)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class PhoneOTP(models.Model):
    phone = models.CharField(max_length=15, db_index=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.code}"

    @staticmethod
    def generate_code():
        return str(random.randint(10000, 99999))
