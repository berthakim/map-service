from django.db import models

class Light(models.Model):
	id_day = models.IntegerField(primary_key=True)
	day_ru = models.CharField(max_length=50)
	sunrise = models.CharField(max_length=25)
	sunet = models.CharField(max_length=20)
	true_noon = models.CharField(max_length=20)
	daylight_hours = models.CharField(max_length=30)
	month_str = models.CharField(max_length=30)
	day_int = models.IntegerField()
	month_int = models.IntegerField()

	def __str__(self):
	    return self.day_ru

class ImageLight(models.Model):
	id_img = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=25)
	img_file = models.FileField(default='')
	source = models.CharField(max_length=100)

	def __str__(self):
	    return self.title
