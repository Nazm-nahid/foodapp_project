from django import forms
from django.core import validators
from foodlist.models import Foodlist
from Rider.models import Rider,Store
class FormName(forms.ModelForm):

    deli_address = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    #phone_no = forms.CharField()

    class Meta:
        model = Rider
        fields = ('deli_address','phone',)

class FormName2(forms.ModelForm):
    quantity = forms.CharField()

    class Meta:
        model = Store
        fields = ('quantity',)

