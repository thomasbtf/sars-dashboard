from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    name = "sars_dashboard.changelog"
    verbose_name = _("Changelog")
    default_auto_field = "django.db.models.BigAutoField"
