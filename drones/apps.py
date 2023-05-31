from django.apps import AppConfig


class DronesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "drones"

    def ready(self):
        from drones import signals  # noqa
