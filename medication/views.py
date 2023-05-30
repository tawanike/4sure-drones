from medication.models import Medicine
from medication.serializers import MedicationSerializer
from rest_framework import generics


class MedicationAPIView(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        return Medicine.objects.filter(user=self.request.user)


class MedicinesAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    queryset = Medicine.objects.all()
    lookup_field = 'id'
