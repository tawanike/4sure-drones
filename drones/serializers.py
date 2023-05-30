from drones.models import Drone
from rest_framework import serializers


class DroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = '__all__'
