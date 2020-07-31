from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from User.models import User
from foodlist.models import Foodlist
@login_required(login_url="/user/login/")
def cart(request):
	context = {

	}
	return render(request, 'Dashboard/cart.html', context)