from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import folium

def health(request):
    m = folium.Map([51.5, -0.25], zoom_start=10)
    test = folium.Html('<b>Hello world</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m = m._repr_html_()
    context = {'map': m}
    return render(request, 'health/health.html', context)
