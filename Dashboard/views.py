from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from User.models import User
from foodlist.models import Foodlist
from . import forms

@login_required(login_url="/user/login/")
def cart(request,food_id):
	form = forms.FormName()
	# food_id = request.POST.get('id')
	context = {
		'form': form,
		'f_id':food_id,
	}
	# print(food_id)
	return render(request, 'Dashboard/cart.html', context)
def abc(request):
	pass