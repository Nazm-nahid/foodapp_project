from django.conf.urls import url
from .import views

urlpatterns =[
    url(r'^ac/$',views.accept, name='accept'),
    url(r'^pay/$',views.payment, name='payment'),
]
