from .models import Product, Service, Reservation, Gallery
from rest_framework import serializers
import jdatetime
from datetime import date


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id",)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        date_str = data.get("date")
        time = data.get("time")

        try:
            y, m, d = map(int, date_str.split('/'))
            selected_date = jdatetime.date(y, m, d).togregorian()
        except Exception:
            raise serializers.ValidationError("فرمت تاریخ نامعتبر است")

        if selected_date < date.today():
            raise serializers.ValidationError("امکان رزرو برای تاریخ گذشته وجود ندارد")

        if Reservation.objects.filter(date=date_str, time=time).exists():
            raise serializers.ValidationError("این روز و ساعت قبلاً رزرو شده است")

        return data


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)


class OtpVerifySerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)
