from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    location = models.PointField(srid=4326,null=True, blank=True,)

    def __str__(self):
        return self.text


