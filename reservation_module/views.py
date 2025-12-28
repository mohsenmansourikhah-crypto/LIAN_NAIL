from django.shortcuts import render
from api_module.models import Reservation
from django.views.generic.list import ListView

# Create your views here.
class ReservationView(ListView):
    model = Reservation
    template_name = "reservation_module/reserve_page.html"
    context_object_name = "reserve"
