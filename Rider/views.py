from django.shortcuts import render
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