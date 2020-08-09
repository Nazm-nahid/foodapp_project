from django.urls import path
from Dashboard import views

urlpatterns = [
    # path('cart/',views.abc),
    path('cart/<int:food_id>', views.cart,name='cart'),
    path('success/<int:food_id>', views.checkout,name='checkout'),
]
