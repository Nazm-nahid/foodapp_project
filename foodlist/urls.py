from django.urls import path 
from Dashboard import views

urlpatterns = [
    path('cart/',views.cart,name='cart'),
]
