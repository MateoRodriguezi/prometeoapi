from django.urls import path
from.views import *

urlpatterns = [
    path('', BankListView.as_view()),
    path('<bank_uuid>', BankDetailView.as_view())
]
