from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from User.forms import UserCreationFormExtended,UserProfileForm
from django.http import HttpResponse
# Create your views here.____________
def signup_user(request):
    if request.method=='POST':
        form = UserCreationFormExtended(request.POST)
        profile = UserProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user= form.save()
            p = profile.save(commit=False)
            p.user = user
            p.save()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                if (user.userprofile.check == 'khadok'):
                    return redirect("reslist")
                else:
                    if (user.userprofile.check == 'rider'):
                        return redirect("riderhome")
                    else:
                        return redirect("storehome")
    else:
        form = UserCreationFormExtended()
        profile = UserProfileForm()
    return render(request,"User/signup.html",{"form":form,"profile" : profile})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                if (user.userprofile.check == 'khadok'):
                    return redirect("reslist")
                else:
                    if (user.userprofile.check == 'rider'):
                        return redirect("riderhome")
                    else:
                        return redirect("storehome")
    else:
        form = AuthenticationForm()
    return render(request, "User/login.html", {"form": form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect("reslist")
#Finish
