from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/user/login/")
def cart(request):
	context = {}
	return render(request, 'Dashboard/cart.html', context)