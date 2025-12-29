from django.urls import path
from .views import ReserveView, ReservedTimesView

urlpatterns = [
    path('', ReserveView.as_view(), name='reserve_page'),
    path('api/reserved-times/', ReservedTimesView.as_view(), name='reserved_times'),
]

