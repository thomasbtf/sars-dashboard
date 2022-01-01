from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    name = "sars_dashboard.samples"
    verbose_name = _("Samples")
    default_auto_field = "django.db.models.BigAutoField"
