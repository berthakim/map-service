from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City, Pop

def weather_map(request):
	pops = Pop.objects.all()

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=969bd7bdde2aa8690b83ebfa2b4056cb'
	
	cities = City.objects.all()  # return all the cities in the database
	
	weather_data = []
	for city in cities:
		city_weather = requests.get(url.format(city.name)).json()  #request the API data and convert the JSON to Python data types
		weather = {
			'city': city,
			'temperature': city_weather['main']['temp'],
			'description': city_weather['weather'][0]['description'],
			'icon': city_weather['weather'][0]['icon']
		}
		weather_data.append(weather)  # add the data for the current city into out list

	context = {'weather_data': weather_data, 'pops': pops}

	return render(request, 'weather_map/weather_map.html', {'pops': pops})
