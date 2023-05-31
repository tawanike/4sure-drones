from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.MedicineAPIView.as_view(), name='medicine'),
    path('', views.MedicinesAPIView.as_view(), name='medicines'),
]
