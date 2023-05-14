from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ProcessPaymentAPIView.as_view(),name='create-payment'), 
    ]