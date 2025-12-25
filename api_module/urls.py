from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    GalleryViewSet,
    ServiceViewSet,
    ReservationViewSet,
    RegisterViewSet,
    VerifyLoginViewSet,
    VerifyRegisterViewSet,
    LoginViewSet
)

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="product")
router.register(r"galleries", GalleryViewSet, basename="gallery")
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"reservations", ReservationViewSet, basename="reservation")
router.register("auth/register", RegisterViewSet, basename="register")
router.register("auth/register/verify", VerifyRegisterViewSet, basename="register-verify")
router.register("auth/login", LoginViewSet, basename="login")
router.register("auth/login/verify", VerifyLoginViewSet, basename="login-verify")

urlpatterns = router.urls
