from .models import Product, Service, Gallery, Reservation
from rest_framework import serializers


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
        if Reservation.objects.filter(
                date=data["date"],
                time=data["time"]
        ).exists():
            raise serializers.ValidationError(
                "این تاریخ و ساعت قبلاً رزرو شده است"
            )
        return data
