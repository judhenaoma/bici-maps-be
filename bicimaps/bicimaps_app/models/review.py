from django.db import models
from .user import User


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    review = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.review