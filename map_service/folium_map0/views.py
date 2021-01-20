from django.shortcuts import render
import folium
from .models import Light


def folium_map0(request):
    m = folium.Map([51.5, -0.25], zoom_start=10)
    test = folium.Html('<b>Hello world</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m = m._repr_html_()

    lights = Light.objects.all()
    context = {'my_map': m, 'lights': lights}

    return render(request, 'folium_map0/folium_map0.html', context)

# source add folium map code: https://stackoverflow.com/questions/50517620/django-and-folium-integration
