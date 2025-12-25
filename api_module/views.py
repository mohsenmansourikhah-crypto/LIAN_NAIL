from django.shortcuts import render
from .models import Product, Service, Reservation, Gallery
from . serializer import ReservationSerializer, ServiceSerializer, GallerySerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer