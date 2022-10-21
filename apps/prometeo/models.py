from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from apps.userapp.models import Account



class BankAccount(models.Model):
    bank_name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)


    def __str__(self):
        return f'{self.bank_name}'
