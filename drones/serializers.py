from drones.models import Drone
from rest_framework import serializers


class DroneSerializer(serializers.ModelSerializer):

    def validate_weight_limit(self, value):
        return value

    class Meta:
        model = Drone
        fields = '__all__'
