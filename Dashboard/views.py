from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from User.models import User
from foodlist.models import Foodlist
from . import forms

@login_required(login_url="/user/login/")
def cart(request,food_id):
	form = forms.FormName()
	form2 = forms.FormName2()
	# food_id = request.POST.get('id')
	context = {
		'form2': form2,
		'form': form,
		'f_id':food_id,
	}
	# print(food_id)
	return render(request, 'Dashboard/cart.html', context)
def checkout(request,food_id):
	if request.method == 'POST':
		form_s = forms.FormName2(request.POST)
		form_r = forms.FormName(request.POST)
		if form_s.is_valid() and form_r.is_valid():
			r = form_r.save(commit=False)
			r.resturent = Foodlist.objects.get(id=food_id).res_id
			r.rider_ac="none"
			r.save()
			s = form_s.save(commit=False)
			s.key = r
			s.resturent = Foodlist.objects.get(id=food_id).res_id
			s.order_item = Foodlist.objects.get(id=food_id).food_name
			s.payment= "No"
			s.phone = r.phone
			s.rider_ac= "none"
			s.save()
	return redirect("reslist")
