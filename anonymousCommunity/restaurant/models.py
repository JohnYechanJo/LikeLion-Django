from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurantPlace=models.CharField(max_length=200)
    restaurantName=models.CharField(max_length=200)
    openDate=models.CharField(max_length=200)
    useStartTime=models.CharField(max_length=200)
    useEndTime=models.CharField(max_length=200)
    breakStartTime=models.CharField(max_length=200)
    breakEndTime=models.CharField(max_length=200)
    foodType=models.CharField(max_length=200)
    restaurantNumber=models.TextField()
    url=models.URLField()
    def __str__(self):
        return self.restaurantName