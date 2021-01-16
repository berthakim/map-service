from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView

def fire(request):
    return render(request, 'fire/fire.html')
