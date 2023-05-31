from __future__ import absolute_import
import os
from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings


logger = get_task_logger(__name__)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
app = Celery('drones')


app.config_from_object('django.conf:settings')
app.conf.timezone = 'UTC'
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "check-battery": {
        "task": "drones.tasks.check_battery_level",
        "schedule": 20.0
    }
}
