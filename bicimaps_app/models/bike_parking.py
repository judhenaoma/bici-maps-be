from django.contrib.gis.db import models
from .user import User


class BikeParking(models.Model):
    parking_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    coordinates = models.PointField(srid=4326)
    img_src = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name