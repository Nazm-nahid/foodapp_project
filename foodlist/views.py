from django.shortcuts import render
from .models import Foodlist
# Create your views here.
def foodview(request,res_id):
    template = 'foodlist/foodlist.html'
    foods=Foodlist.objects.all()
    list_foods=foods.filter(res_id=res_id)
    
    return render(request,template,{"foods":list_foods})