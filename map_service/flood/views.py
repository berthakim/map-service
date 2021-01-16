from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import ...

from django.http import HttpResponse
from django.views.generic import TemplateView

def flood(request):
    return render(request, 'flood/flood.html')
