from django.urls import path

from . import views

urlpatterns = [
    path('/<int:id>', views.DroneAPIView.as_view(), name='drone'),
    path('/<int:drone>/load', views.DroneLoadAPIView.as_view(), name='drone-load'),
    path('/<int:drone>/battery', views.DroneBatteryAPIView.as_view(), name='drone-battery'),
    path('', views.DronesAPIView.as_view(), name='drones'),
]
