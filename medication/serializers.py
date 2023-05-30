from medication.models import Medicine
from rest_framework import serializers


class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = '__all__'
