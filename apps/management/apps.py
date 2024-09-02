# .\apps\management\apps.py
from django.apps import AppConfig


class ManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.management"
    label = "management"

    def ready(self):
        import apps.core.signals  # noqa: F401
