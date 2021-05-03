from django.shortcuts import render,redirect
from store.models import *
from store.utils import cookieCart, cartData
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from ecommerce.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from users.forms import UserRegisterForm
import random
from store import forms

##########################
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.serializers import productSerializer

#************************************ For Index.html **************************************************
def index(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products,'cartItems':cartItems}
	return render(request, 'index.html', context)

#************************************ For Store.html **************************************************
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store.html', context)

#*********************************** For productdetail.html **********************************************
class ItemDetailView(DetailView):
    model = Product
    template_name = "productdetail.html"

#*********************************** For Contact.html **********************************************
def contact(request):
	return render(request,'contact.html')

#*********************************** For Cart.html **********************************************
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

#*********************************** For Checkout.html **********************************************
@login_required
def checkout(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

#*********************************** For the mail after payment is done **********************************************
def paymentdonemail(request):

	messages.success(request, 'Congratulations! The order has been successfully Booked!')

	subject = 'Payment Successful'
	usr_orderid = random.randint(100000,999999)
	UserOrderId.objects.create(OrderId= usr_orderid)
	message = 'Payment has been successfully done.Your OrderID is = '+ str(usr_orderid)
	recepient = str(request.user.email)
	send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
	return redirect('index')

#****************************** For Tracking Order-ID ****************************************************************8
def trackorder(request):

	# if DeliveryPersonData.objects.filter(DId = form.cleaned_data['OrderId']).exists():
	# 	return render(request,'track.html',{'DeliveryPersonData':DeliveryPersonData})
	DeliveryPersonID = request.POST.get("head3.outerText")
	print(DeliveryPersonID)
	deliveryPersonData = DeliveryPersonData.objects.all()
	context = {'deliveryPersonData':deliveryPersonData, "deliveryPersonID": DeliveryPersonID}
	return render(request,'track.html',context)

def trackorderid(request):
	if request.method == 'POST':
		form = forms.OrderIdCheckForm(request.POST)

		if form.is_valid(): #details r correctly filled check
			if UserOrderId.objects.filter(OrderId = form.cleaned_data['OrderId']).exists():
				return redirect('trackorder')
			else:
				messages.error(request, 'Sorry, Wrong Order-ID')
				return redirect('trackorderid')

	else:
		form = forms.OrderIdCheckForm()
		return render(request,'orderidcheck.html', { 'form':form })

###################################################################################################

class ProductList(APIView):

	def get(self,request):
		product1 = Product.objects.all()
		serializer = productSerializer(product1, many=True)
		return Response(serializer.data)

	def post(self):
		pass


# DeliveryPersonData.objects.create(DId= ) //USED to save data in DeliveryPersonData

# if DeliveryPersonData.objects.filter(DId = form.cleaned_data['OrderId']).exists():  //
