from drones.models import Drone
from drones.serializers import DroneSerializer
from loads.models import Load
from rest_framework import serializers

from medication.serializers import MedicationSerializer


class LoadSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # TODO: Handle payloads with more than one item but less than weight limit
        drone = validated_data.get('drone')
        payload = validated_data.get('payload')

        if drone.battery_capacity < Drone.BATTERY_CAPACITY_LIMIT:
            raise serializers.ValidationError({"error": "Drone battery too low to load payload."})

        else:
            # Drone state can transition to loading if it is in idle state else raise error
            if drone.state == Drone.IDLE:
                drone.state = Drone.LOADING
                drone.save()
            else:
                raise serializers.ValidationError({"error": "Drone already in loading state."})

        # Try to load payload
        if payload.weight > drone.weight_limit:
            raise serializers.ValidationError(
                {"error": 'Payload weight exceeds drone weight limit.'})

        if drone.state != Drone.LOADING:
            raise serializers.ValidationError({"error": "Drone is not ready for payload."})

        # If no errors transition drone state to loaded
        drone.state = Drone.LOADED
        drone.save()

        return validated_data

    class Meta:
        model = Load
        fields = '__all__'
