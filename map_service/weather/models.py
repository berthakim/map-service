from django.db import models

class City(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):  # show the actual city name on the dashboard
	    return self.name

	class Meta:  # show the plural of city as cities instead of cities
	    verbose_name_plural = 'cities'

'''
This will create a table in our database that will have a 
column called name, which is the name of the city. 
This city will be a charfield,  which is just a string.
'''
