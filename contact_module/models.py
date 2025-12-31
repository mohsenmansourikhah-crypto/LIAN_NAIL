from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="عنوان پیام",
        blank=True
    )
    full_name = models.CharField(max_length=100, verbose_name="نام کاربر")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس کاربر")
    message = models.TextField(verbose_name="پیام کاربر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"
