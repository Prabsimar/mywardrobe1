from django import forms
from .models import UserOrderId

class OrderIdCheckForm(forms.Form):
    OrderId = forms.IntegerField(label="Enter your Order ID ")

# class DeliveryPersonId(forms.form):
# 	PersonId = forms.IntegerField()
