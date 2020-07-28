from django.urls import path 
from . import views
import foodlist.views

urlpatterns = [
    path('',views.resview,name="reslist"),
    path('<int:res_id>/',foodlist.views.foodview,name="resdetail"),
]
