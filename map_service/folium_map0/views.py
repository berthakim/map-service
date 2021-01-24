from django.shortcuts import render
import folium
from .models import Light, ImageLight
import datetime


def folium_map0(request):
    # map
    m = folium.Map([51.5, -0.25], zoom_start=10)
    test = folium.Html('<b>Hello world</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m = m._repr_html_()

    # access to the data from DB (light and imgs_light)
    lights = Light.objects.all()
    img_lights = ImageLight.objects.all()

    # light. define the current date (day and month)
    now = datetime.datetime.now()
    now_day, now_month = now.day, now.month
    now_hour, now_min = now.hour, now.minute

    context = {'my_map': m, 'lights': lights, 'now_day': now_day,
               'now_month': now_month, 'img_lights': img_lights, 
               'now_hour': now_hour, 'now_min':now_min}

    return render(request, 'folium_map0/folium_map0.html', context)
