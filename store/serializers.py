from rest_framework import serializers
from store.models import Product

class productSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		#fields={'name','price','image','discount_price','featured','slug','description'}
		fields='__all__'

###########################################