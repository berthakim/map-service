from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def desc(request):
    return render(request, 'descriptions/desc.html')
