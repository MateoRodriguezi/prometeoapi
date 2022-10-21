from django.shortcuts import render, get_object_or_404
from apps.userapp.models import Account

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


from django.db.models.query_utils import Q

from .models import BankAccount
from .serializers import BankAccountSerializer

class BankListView(APIView):
    def get (self, request, format=None):
        if BankAccount:
            
            serializer = BankAccountSerializer ()

            return Response({'bankaccounts': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No bankaccounts founds'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BankDetailView(APIView):
    def get(self, request, format=None):
        bank = get_object_or_404(BankAccount)
        serializer = BankAccountSerializer(bank)
        return Response({'bank':serializer.data}, status=status.HTTP_200_OK)