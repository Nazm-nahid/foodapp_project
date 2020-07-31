from django.conf.urls import url
from .import views

urlpatterns =[
    url(r'^riderhome/$',views.riderview, name='riderhome'),
    url(r'^storehome/$',views.storeview, name='storehome'),
    url(r'^myride/$',views.rideraccept, name='myride'),
    url(r'^ac/(?P<slug>[\w-]+)/$',views.accept, name='accept'),
    url(r'^pay/(?P<slug>[\w-]+)/$',views.payment, name='payment'),
]
