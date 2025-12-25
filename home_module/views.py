from django.shortcuts import render
from django.contrib.auth.views import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = "home_module/home_page.html"
