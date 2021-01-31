from django.shortcuts import render

from requests import get
import json
import folium
import os
import webbrowser
import html

url = 'your API token'

stations = get(url).json()

temps, pres, humid, wind, desc, icon = [], [], [], [], [], []
tmax = 0.0
tmin = 100.0
lons = [station['coord']['lon'] for station in stations['list']]
lats = [station['coord']['lat'] for station in stations['list']]
wsnames = [html.escape(station['name']) for station in stations['list']]
for data in stations['list']:
    t = data['main']['temp']
    p = data['main']['pressure']
    h = data['main']['humidity']
    w = data['wind']['speed']
    d = data['weather'][0]['description']
    i = data['weather'][0]['icon']
    temps.append(str(t))
    pres.append(str(p))
    humid.append(str(h))
    wind.append(str(w))
    desc.append(str(d))
    icon.append(str(i))

def colourgrad(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    g = int(max(0, 255*(ratio - 1)))
    r = 255 - b - g
    hexcolour = '#%02x%02x%02x' % (r,g,b)
    return hexcolour

def folium_map(request): 
    m = folium.Map(location=[47.5, 2.5], zoom_start=9)
    for n in range(len(lons)-1):
        hcol = colourgrad(tmin, tmax, float(temps[n]))
        folium.CircleMarker([lats[n], lons[n]],
                            radius = 5,
                            popup = wsnames[n]+': '+
                            '\nTemperature: ' + temps[n]+
                            '\nPressure: ' + pres[n]+
                            '\nHumidity: ' + humid[n]+
                            '\nWind speed: ' + wind[n]+
                            '\nDesc: ' + desc[n]+
                            '\nIcon: ' + icon[n],
                            fill_color = hcol).add_to(m)
    m = m._repr_html_()
    context = {'weather_f_map': m}
    return render(request, 'folium_map/folium_map.html', context)
