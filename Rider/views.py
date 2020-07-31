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
    items = riders.filter(rider_ac='none')
    if (request.user.userprofile.check == 'rider'):
        return render(request, template, {"riders": items})
    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def rideraccept(request):
    template = 'Rider/myride.html'
    riders = Rider.objects.all()
    items = riders.filter(rider_ac=request.user)
    if (request.user.userprofile.check == 'rider'):
        return render(request, template, {"riders": items})
    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def storeview(request):
    template = 'Rider/storehome.html'
    stores = Store.objects.all()
    list_items = stores.filter(resturent=request.user)
    if (request.user.userprofile.check == 'store'):
        return render(request, template, {"items": list_items})
    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def accept(request,slug):
    if (request.user.userprofile.check == 'rider'):
        if request.method == 'POST':
            t = Rider.objects.get(id=slug)
            u=request.user
            t.rider_ac=str(u)
            t.save()
            t2=Store.objects.get(key=str(slug))
            t2.rider_ac = str(u)
            t2.save()
            template = 'Rider/riderhome.html'
            riders = Rider.objects.all()
            items = riders.filter(rider_ac='none')
            return render(request, template, {"riders": items})

    else:
        return HttpResponse('Illigal Action!!!')

@login_required(login_url="/user/login/")
def payment(request,slug):
    if (request.user.userprofile.check == 'store'):
        if request.method == 'POST':
            t2 = Store.objects.get(key=str(slug))
            t2.payment = 'Yes'
            t2.save()
            template = 'Rider/storehome.html'
            stores = Store.objects.all()
            list_items = stores.filter(resturent=request.user)
            return render(request, template, {"items": list_items})
    else:
        return HttpResponse('Illigal Action!!!')
