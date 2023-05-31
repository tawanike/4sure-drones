from django.db import models


class BatteryStatus(models.Model):
    drone = models.ForeignKey(
        "drones.Drone", related_name="drone_battery_status", on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'battery_status'
        verbose_name = 'Battery Status Movement'
        verbose_name_plural = 'Battery Status Movement'

    def __str__(self) -> str:
        return f"{self.drone} - {self.level}"


# Create your models here.
class Drone(models.Model):
    BATTERY_CAPACITY_LIMIT = 25

    LIGHTWEIGHT = 'lightweight'
    MIDDLEWEIGHT = 'middleweight'
    CRUISERWEIGHT = 'cruiserweight'
    HEAVYWEIGHT = 'heavyweight'

    IDLE = 'idle'
    LOADING = 'loading'
    LOADED = 'loaded'
    DELIVERING = 'delivering'
    DELIVERED = 'delivered'
    RETURNING = 'returning'

    DRONE_MODEL_CHOICES = (
        (LIGHTWEIGHT, 'Lightweight'),
        (MIDDLEWEIGHT, 'Middleweight'),
        (CRUISERWEIGHT, 'Cruiserweight'),
        (HEAVYWEIGHT, 'Heavyweight'),
    )

    DRONE_STATE_CHOICES = (
        (IDLE, 'Idle'),
        (LOADING, 'Loading'),
        (LOADED, 'Loaded'),
        (DELIVERING, 'Delivering'),
        (DELIVERED, 'Delivered'),
        (RETURNING, 'Returning'),
    )
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=15, choices=DRONE_MODEL_CHOICES)
    state = models.CharField(max_length=15, default=IDLE, choices=DRONE_STATE_CHOICES)
    weight_limit = models.DecimalField(max_digits=5, decimal_places=2)  # 500gr max
    battery_capacity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'drones'
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self) -> str:
        return self.serial_number


class DroneStatusMovement(models.Model):
    drone = models.ForeignKey(
        "drones.Drone", related_name="drone_status_movement", on_delete=models.CASCADE)
    status = models.CharField(max_length=15, default=Drone.IDLE, choices=Drone.DRONE_STATE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'drone_status_movement'
        verbose_name = 'Drone Status Movement'
        verbose_name_plural = 'Drone Status Movement'

    def __str__(self) -> str:
        return f"{self.drone} - {self.status}"
