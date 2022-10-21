from unicodedata import category
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=[
            'name',
            'birthday',
            'address',
            'city',
            'country',
        ]