from django.shortcuts import render
from api_module.models import Gallery
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class GalleryView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = "gallery_module/gallery_page.html"
    context_object_name = "galleries"
    login_url = "login_page"

