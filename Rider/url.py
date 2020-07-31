from django.conf.urls import url
from .import views

urlpatterns =[
    url(r'^riderhome/$',views.riderview, name='riderhome'),
    url(r'^storehome/$',views.storeview, name='storehome'),
    url(r'^ac/$',views.accept, name='accept'),
    url(r'^pay/$',views.payment, name='payment'),
]
