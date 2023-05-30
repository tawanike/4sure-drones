from drones.models import Drone
from drones.serializers import DroneSerializer
from rest_framework import generics


class DronesAPIView(generics.ListCreateAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()


class DroneAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()
    lookup_field = 'id'
