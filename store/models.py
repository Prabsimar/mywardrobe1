from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.forms import ModelForm

# ******************************Used in views.store and views.ItemDetailView *********************
class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(blank=False)
	image = models.ImageField(blank=False)
	discount_price = models.FloatField(blank=False)
	featured = models.BooleanField(default=False)

	slug = models.SlugField(blank=False,unique=True)
	description = models.TextField(blank=False)



	def get_absolute_url(self):
		return reverse("product", kwargs={ 'slug': self.slug})

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class UserOrderId(models.Model):

	OrderId = models.IntegerField()

class DeliveryPersonData(models.Model):
	DId = models.IntegerField(blank=False) 
	DName = models.CharField(max_length=200,blank=False)
	DMobile = models.IntegerField(blank=False)
	DPhoto = models.ImageField(blank=False)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

