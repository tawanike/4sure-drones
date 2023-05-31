from django.db import models

from drones.models import Drone
from medication.models import Medicine

# Create your models here.


class Load(models.Model):
    drone = models.ForeignKey(Drone, related_name="drone_load", on_delete=models.CASCADE)
    payload = models.ForeignKey(Medicine, related_name="drone_payload", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'loads'
        verbose_name = 'Load'
        verbose_name_plural = 'Loads'

    def __str__(self) -> str:
        return f"{self.drone} - {self.payload}"


class LoadStatusMovement(models.Model):
    load = models.ForeignKey(Load, related_name="load_status", on_delete=models.CASCADE)
    state = models.CharField(max_length=50, default=Drone.IDLE, choices=Drone.DRONE_STATE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'load_status_movement'
        verbose_name = 'Load Status Movement'
        verbose_name_plural = 'Load Status Movements'

    def __str__(self) -> str:
        return f"{self.drone} - {self.payload}"
