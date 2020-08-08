from django.urls import path ,include
from . import views
import foodlist.views
import foodlist
urlpatterns = [
    path('',views.resview,name="reslist"),
    path('<int:res_id>/',foodlist.views.foodview,name="resdetail"),
]



