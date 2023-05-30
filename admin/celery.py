from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.conf import settings


logger = get_task_logger(__name__)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
app = Celery('flemoji')


app.config_from_object('django.conf:settings')
app.conf.timezone = 'UTC'
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "send-emails": {
        "task": "altur.email.tasks.task_send_emails",
        "schedule": 20.0
    },
    "send-sms": {
        "task": "altur.sms.tasks.task_send_smses",
        "schedule": 30.0
    },
    "send-push-notifications": {
        "task": "altur.push.tasks.task_send_push_notifications",
        "schedule": 40.0
    },
    "update_stats": {
        "task": "mmogo.profiles.tasks.task_update_stats",
        "schedule": crontab(minute='*/1')
    },
    "reindex_search": {
        "task": "mmogo.contrib.search.tasks.task_reindex_search",
        "schedule": crontab(minute='*/1')
    }
}
