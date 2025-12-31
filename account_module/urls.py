from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register_page"),
    path("register/verify/", views.register_verify_view, name="register_verify"),
    path("register/success/", views.register_success_view, name="register_success"),
    path("login/", views.login_view, name="login_page"),
    path("login/verify/", views.login_verify_view, name="login_verify"),
    path("login/success/", views.login_success_view, name="login_success"),
    path("logout/", views.logout_view, name="logout_page")
]
