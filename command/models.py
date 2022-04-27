from django.db import models


# Create your models here.
class Command(models.Model):
    command = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
