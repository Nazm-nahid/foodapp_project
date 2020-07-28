from django.db import models

class Rider(models.Model):
    resturent=models.CharField(max_length=200)
    deli_address= models.CharField(max_length=400)
    time= models.TimeField( )
    rider_ac= models.CharField(max_length=200)
    def __str__(self):
        return self.id
class Store(models.Model):
    id = models.ForeignKey(Rider, on_delete=models.CASCADE)
    resturent=models.CharField(max_length=200)
    order_item= models.CharField(max_length=50)
    time= models.TimeField( )
    payment= models.CharField(max_length=3)
    rider_ac= models.CharField(max_length=200)
    def __str__(self):
        return self.resturent
