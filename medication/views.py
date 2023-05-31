from medication.models import Medicine
from medication.serializers import MedicationSerializer
from rest_framework import generics


class MedicinesAPIView(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
    queryset = Medicine.objects.all()


class MedicineAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    queryset = Medicine.objects.all()
    lookup_field = 'id'
