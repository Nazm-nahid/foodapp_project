from django import forms
from django.core import validators
from foodlist.models import Foodlist
from Rider.models import Rider,Store
class FormName(forms.Form):
    quantity = forms.CharField()
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    phone_no = forms.CharField()


