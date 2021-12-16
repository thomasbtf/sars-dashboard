from django.apps import AppConfig


class ReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reports"

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals  # noqa F401
