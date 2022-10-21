from urllib.parse import MAX_CACHE_SIZE
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True) 
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=20, blank=True)