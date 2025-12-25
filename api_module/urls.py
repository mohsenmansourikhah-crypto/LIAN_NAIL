from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    GalleryViewSet,
    ServiceViewSet,
    ReservationViewSet,
)

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="product")
router.register(r"galleries", GalleryViewSet, basename="gallery")
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"reservations", ReservationViewSet, basename="reservation")

urlpatterns = router.urls