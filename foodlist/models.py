from django.db import models
from reslist.models import Res
# Create your models here.
class Foodlist(models.Model):
    res_id=models.ForeignKey(Res,on_delete=models.DO_NOTHING)
    food_image=models.ImageField(upload_to="food_images/")
    food_name=models.CharField(max_length=200)
    food_info=models.CharField(max_length=300,null=True)
    price=models.IntegerField()
    def __str__(self):
        return self.food_name
