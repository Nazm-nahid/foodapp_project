from django.shortcuts import render
from .models import Rider,Store
from django.http import HttpResponse


# Create your views here.
def riderview(request):
    template = 'Rider/riderhome.html'
    riders = Rider.objects.all()

    return render(request, template, {"riders": riders})

def storeview(request):
    template = 'Rider/storehome.html'
    list_items = Store.objects.all()

    return render(request, template, {"items": list_items})


def accept(request):
    if request.method == 'POST':
        return HttpResponse('Accepted')


def payment(request):
    if request.method == 'POST':
        return HttpResponse('Payment Done')
