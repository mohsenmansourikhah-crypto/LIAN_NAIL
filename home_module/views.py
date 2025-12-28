from django.shortcuts import render
from .models import Slider
from django.contrib.auth.views import TemplateView
from api_module.models import Gallery, Service, Product
from django.views.generic.list import ListView


# Create your views here.
class HomeView(TemplateView):
    template_name = "home_module/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Slider.objects.all()
        return context


class HeaderComponent(TemplateView):
    template_name = "shared/header_component.html"


class FooterComponent(TemplateView):
    template_name = "shared/footer_component.html"


class GalleryHomeView(ListView):
    model = Gallery
    template_name = "home_module/gallery_home.html"
    context_object_name = "galleries"

class ServiceHomeView(ListView):
    model = Service
    template_name = "home_module/service_home.html"
    context_object_name = "services"

class ProductHomeView(ListView):
    model = Product
    template_name = "home_module/product_home.html"
    context_object_name = "products"
