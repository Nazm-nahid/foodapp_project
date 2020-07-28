from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES= [
    ('khadok','Register as a User'),
    ( 'rider','Register as a Rider'),
    ( 'store','Register as a Store'),
    ]

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    check = models.CharField(max_length=30,choices=CHOICES)


    def __str__(self):
        return self.user.username 
