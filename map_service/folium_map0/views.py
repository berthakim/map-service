from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic import TemplateView
# from requests import get
import folium


def folium_map0(request):
    m = folium.Map([51.5, -0.25], zoom_start=10)
    test = folium.Html('<b>Hello world</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m = m._repr_html_()  # updated
    context = {'my_map': m}

    return render(request, 'folium_map0/folium_map0.html', context)

# source: https://stackoverflow.com/questions/50517620/django-and-folium-integration

#-------------------------

# def folium_map0(request):
#     return render(request, 'folium_map/folium_map.html')

# class FoliumView(TemplateView):
#     template_name = "folium_map/folium_map.html"

#     def get_context_data(self, **kwargs):
#         figure = folium.Figure()
#         m = folium.Map(
#             location=[45.372, -121.6972],
#             zoom_start=12,
#             tiles='Stamen Terrain'
#         )
#         m.add_to(figure)

#         folium.Marker(
#             location=[45.3288, -121.6625],
#             popup='Mt. Hood Meadows',
#             icon=folium.Icon(icon='cloud')
#         ).add_to(m)

#         folium.Marker(
#             location=[45.3311, -121.7113],
#             popup='Timberline Lodge',
#             icon=folium.Icon(color='green')
#         ).add_to(m)

#         folium.Marker(
#             location=[45.3300, -121.6823],
#             popup='Some Other Location',
#             icon=folium.Icon(color='red', icon='info-sign')
#         ).add_to(m)
#         figure.render()
#         return {"map": figure}
