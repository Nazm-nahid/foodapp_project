from django.shortcuts import render
from .models import Rider,Store
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/user/login/")
def riderview(request):
    template = 'Rider/riderhome.html'
    riders = Rider.objects.all()
    if (request.user.userprofile.check == 'rider'):
        return render(request, template, {"riders": riders})
    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def storeview(request):
    template = 'Rider/storehome.html'
    list_items = Store.objects.all()
    if (request.user.userprofile.check == 'store'):
        return render(request, template, {"items": list_items})
    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def accept(request):
    if (request.user.userprofile.check == 'rider'):
        if request.method == 'POST':
            return HttpResponse('Accepted')
    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def payment(request):
    if (request.user.userprofile.check == 'rider'):
        if request.method == 'POST':
            return HttpResponse('Payment Done')
    else:
        return HttpResponse('Illigal Action!!!')
