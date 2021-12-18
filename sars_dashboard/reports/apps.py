from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    name = "sars_dashboard.reports"
    verbose_name = _("Reports")
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        try:
            import sars_dashboard.reports.signals  # noqa F401
        except ImportError:
            pass
