
from django.db import models

from django.contrib.auth.models import User


"""class Favorites(models.Model):
    budget = models.DecimalField(max_digits=20,decimal_places=0,null=False,verbose_name="Budget du voyage")
    travel_date_start = models.DateField(verbose_name="Date de Demarrage du voyage")
    travel_date_end = models.DateField(verbose_name="Date de Retour du voyage")
    prefered_activitties = models.JSONField()
    users = models.ManyToManyField(to=User,related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)"""


class Favorites(models.Model):
    users = models.ManyToManyField(to=User,related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    #type_travel = models.CharField(max_length=1000)
    subType = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    deteailedName = models.CharField(max_length=1000)
    id = models.CharField(max_length=100, primary_key= True, unique= True)
    self = models.JSONField()
    timeZoneOffset = models.TimeField()
    iataCode = models.CharField(max_length=63)
    geoCode = models.JSONField()
    address = models.JSONField()
    analytics = models.JSONField()
    users = models.ManyToManyField(to=User,related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'ID : {self.id} - Type : {self.type_travel}- name : {self.name}'



