from django.apps import AppConfig


class LoadsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loads"

    def ready(self):
        from loads import signals  # noqa
