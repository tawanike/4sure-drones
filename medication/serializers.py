from medication.models import Medicine
from rest_framework import serializers
import re


class MedicationSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if not re.match(r'^[A-Za-z0-9_-]+$', value):
            raise serializers.ValidationError(
                "Only letters, numbers, underscores or hyphens are allowed.")
        return value

    def validate_code(self, value):
        if not re.match(r'^[A-Z0-9_-]+$', value):
            raise serializers.ValidationError(
                "Only uppercase letters, numbers and underscores are allowed.")
        return value

    class Meta:
        model = Medicine
        fields = '__all__'
