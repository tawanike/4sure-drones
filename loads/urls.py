from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.MedicationAPIView.as_view(), name='medication'),
    path('', views.MedicinesAPIView.as_view(), name='medicines'),
]
