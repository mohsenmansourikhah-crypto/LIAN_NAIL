from django.shortcuts import render
from api_module.models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class ProductView(ListView):
    model = Product
    template_name = "product_module/product_page.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_module/product_detail.html"
    context_object_name = "product"
