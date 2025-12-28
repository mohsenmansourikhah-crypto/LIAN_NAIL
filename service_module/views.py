from django.shortcuts import render
from django.views.generic.list import ListView
from api_module.models import Service

# Create your views here.
class ServiceView(ListView):
    model = Service
    template_name = "service_module/service_page.html"
    context_object_name = "services"
