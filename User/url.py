from django.conf.urls import url
from .import views

urlpatterns =[
    url(r'^login/$',views.login_user, name='login_user'),
    url(r'^logout/$',views.logout_user, name='logout'),
    url(r'^signup/$',views.signup_user, name='signup_user'),
]