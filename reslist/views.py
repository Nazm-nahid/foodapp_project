from django.shortcuts import render
from .models import Res
# Create your views here.
def resview(request):
    template = 'reslist/reslist.html'
    r=Res.objects
    return render(request,template,{"rl":r})
