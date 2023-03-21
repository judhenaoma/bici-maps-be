from django.contrib.gis.db import models
from .user import User


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field="email" ,on_delete=models.CASCADE, null=True, blank=True)
    review_location = models.PointField(geography=True, srid=4326, blank=True, null=True)
    review = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.review