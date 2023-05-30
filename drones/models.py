from django.db import models


# Create your models here.
class Drone(models.Model):
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
    state = models.CharField(max_length=15, choices=DRONE_STATE_CHOICES)
    weight_limit = models.DecimalField(max_digits=5, decimal_places=2)  # 500gr max
    battery_capacity = models.IntegerField(default=0)

    class Meta:
        db_table = 'drones'
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self) -> str:
        return self.serial_number
