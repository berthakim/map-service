'''
We have to allow the user to add a city directly in the form.

To do that, we need to create a form. We could create the form directly, 
but since our form will have exactly the same field as our model, 
we can use a ModelForm
'''

from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name']
		widgets = {
		    'name': TextInput(attrs={'class': 'input', 'placehlder': 'City Name'}),
		}  # update the input class to have the correct Bulma class and placeholder
