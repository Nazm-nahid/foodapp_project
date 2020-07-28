from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile



class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(UserCreationFormExtended, self).save( commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


CHOICES = [
        ('khadok', 'Register as a User'),
        ('rider', 'Register as a Rider'),
        ('store', 'Register as a Store'),
    ]
class UserProfileForm(forms.ModelForm):
    check = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = UserProfile
        fields = ('check',)
