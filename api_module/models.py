from django.db import models
from django_jalali.db import models as jmodels


# --------------------
# PRODUCT
# --------------------
class Product(models.Model):
    title = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name="عنوان محصول"
    )
    price = models.PositiveIntegerField(
        verbose_name="قیمت محصول (تومان)"
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="تصویر محصول"
    )
    description = models.TextField(
        verbose_name="توضیحات محصول"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال / غیرفعال"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


# --------------------
# SERVICE
# --------------------
class Service(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="عنوان خدمات"
    )
    image = models.ImageField(
        upload_to="services/",
        verbose_name="تصویر خدمات"
    )
    price = models.PositiveIntegerField(
        verbose_name="قیمت خدمات (تومان)"
    )
    description = models.TextField(
        verbose_name="توضیحات خدمات"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال / غیرفعال"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"


# --------------------
# GALLERY
# --------------------
class Gallery(models.Model):
    caption = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="عنوان تصویر"
    )
    image = models.ImageField(
        upload_to="gallery/",
        verbose_name="تصویر"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال / غیرفعال"
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری تصاویر"


# --------------------
# RESERVATION (شمسی)
# --------------------
class Reservation(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="نام مشتری"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="شماره تماس"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="خدمات"
    )

    date = jmodels.jDateField(
        verbose_name="تاریخ رزرو")
    time = models.TimeField(
        verbose_name="ساعت رزرو"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت"
    )

    def __str__(self):
        return f"{self.full_name} - {self.date} {self.time}"

    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزروها"
        unique_together = ("date", "time")
