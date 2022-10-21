from unicodedata import category
from rest_framework import serializers
from .models import BankAccount
from apps.userapp.serializers import AccountSerializer

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankAccount
        fields=[
            'bank_name',
            'country',
        ]