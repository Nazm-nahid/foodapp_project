from django.db import models

class Rider(models.Model):
    resturent=models.CharField(max_length=200)
    deli_address= models.CharField(max_length=400)
    time= models.TimeField( )
    phone = models.CharField(max_length=13)
    rider_ac= models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
class Store(models.Model):
    key = models.ForeignKey(Rider, on_delete=models.CASCADE)
    resturent = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    order_item= models.CharField(max_length=50)
    quantity= models.CharField(max_length=4)
    time= models.TimeField()
    payment= models.CharField(max_length=3)
    rider_ac= models.CharField(max_length=200)
    def __str__(self):
        return self.resturent
