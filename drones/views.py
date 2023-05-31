from drones.models import Drone
from drones.serializers import DroneSerializer
from loads.models import Load
from loads.serializers import LoadSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class DronesAPIView(generics.ListCreateAPIView):
    serializer_class = DroneSerializer

    def get_queryset(self):
        state = self.request.GET.get('state', None)
        if state:
            return Drone.objects.filter(state=state)
        else:
            return Drone.objects.all()


class DroneAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()
    lookup_field = 'id'


class DroneLoadAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LoadSerializer
    lookup_field = 'drone'

    def get(self, request, drone):
        queryset = Load.objects.filter(drone__id=self.request.data.get('drone'),
                                       drone__state=Drone.LOADED).first()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, drone):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": str(serializer.errors.get('payload'))},
                            status=status.HTTP_400_BAD_REQUEST)


class DroneBatteryAPIView(generics.RetrieveAPIView):
    serializer_class = DroneSerializer
    lookup_field = 'drone'

    def get(self, request, drone):
        selected_drone = Drone.objects.get(id=drone)

        return Response({
            "level": selected_drone.battery_capacity
        }, status=status.HTTP_200_OK)
