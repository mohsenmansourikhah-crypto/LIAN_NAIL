from django.shortcuts import render
from api_module.models import Gallery
from django.views.generic.list import ListView
# Create your views here.


class GalleryView(ListView):
    model = Gallery
    template_name = "gallery_module/gallery_page.html"
    context_object_name = "galleries"
