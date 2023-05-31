from medication.models import Medicine
from rest_framework import serializers


class MedicationSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        return value

    def validate_code(self, value):
        return value

    class Meta:
        model = Medicine
        fields = '__all__'
