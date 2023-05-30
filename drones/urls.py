from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.DroneAPIView.as_view(), name='drone'),
    path('', views.DronesAPIView.as_view(), name='drones'),
]
