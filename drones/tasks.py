from admin.celery import app
from celery.utils.log import get_task_logger

from drones.models import Drone, BatteryStatus

logger = get_task_logger(__name__)


@app.task(bind=True)
def check_battery_level(*args):
    drones = Drone.objects.all()
    for drone in drones:
        BatteryStatus.objects.create(
            drone=drone,
            level=drone.battery_capacity
        )
