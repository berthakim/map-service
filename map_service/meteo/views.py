from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def meteo(request):
    return render(request, 'meteo/meteo.html')
