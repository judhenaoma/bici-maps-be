# from django.db import models
from django.contrib.gis.db import models

class Route(models.Model):
    route_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    route = models.MultiLineStringField(srid=4326)
    description = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


