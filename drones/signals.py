from django.db.models.signals import post_save
from django.dispatch import receiver

from drones.models import Drone, BatteryStatus, DroneStatusMovement


@receiver(post_save, sender=Drone)
def update_drone_battery_capacity_change(sender, **kwargs):
    # write you functionality
    drone = kwargs.get('instance')
    BatteryStatus.objects.create(
        drone=drone,
        level=drone.battery_capacity
    )

    DroneStatusMovement.objects.create(
        drone=drone,
        status=drone.state
    )
