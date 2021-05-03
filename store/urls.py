from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('products/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('contact/',views.contact,name="contact"),
	path('checkout/', views.checkout, name="checkout"),
	path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
	path('paymentdonemail', views.paymentdonemail, name='paymentdonemail'),
	path('orderidcheck/',views.trackorderid, name='trackorderid'),
	path('track/',views.trackorder, name='trackorder'),
	#########################################################################
	path('productapi',views.ProductList.as_view()),
	#now we just have to through this url and  connect to any website database and get product data


]
