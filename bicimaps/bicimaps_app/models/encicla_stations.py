from django.contrib.gis.db import models
from .review import Review

class EnciclaStations(models.Model):
    station_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    coordinates = models.PointField(srid=4326)
    img_src = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.name