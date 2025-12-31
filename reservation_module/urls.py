from django.urls import path
from .views import ReserveView, ReservedTimesView, ReserveSuccessView

urlpatterns = [
    path('', ReserveView.as_view(), name='reserve_page'),
    path('reserve/success/', ReserveSuccessView.as_view(), name='reserve_success'),
    path('api/reserved-times/', ReservedTimesView.as_view(), name='reserved_times'),
]

