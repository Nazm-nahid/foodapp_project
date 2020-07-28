from django.shortcuts import render, redirect
from .models import Rider,Store


# Create your views here.
def riderview(request):
    template = 'Rider/riderhome.html'
    riders = Rider.objects.all()

    return render(request, template, {"riders": riders})

def storeview(request, resturent):
    template = 'Rider/storehome.html'
    stores = Store.objects.all()
    list_items = stores.filter(resturent=resturent)

    return render(request, template, {"items": list_items})

def ac(request, _ ):
    if request.method=='POST':
        t = Rider.objects.get(id=_)
        t.rider_ac = user
        t.save()
        r = Store.objects.get(id=_)
        r.rider_ac = user
        r.save()
        
def pay(request, _ ):
    if request.method=='POST':
        r = Store.objects.get(id=_)
        r.payment = 'Done'
        r.save()
