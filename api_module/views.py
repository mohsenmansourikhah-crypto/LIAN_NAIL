from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Product, Service, Reservation, Gallery
from . serializer import ReservationSerializer, ServiceSerializer, GallerySerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet
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