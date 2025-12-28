from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان اسلایدر")
    image = models.ImageField(upload_to="slider/", verbose_name="تصویر اسلایدر")
    description = models.TextField(verbose_name="توضیحات اسلایدر")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیر فعال")


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "تصویر اسلایدر"
        verbose_name_plural = "تصاویر اسلایدر"