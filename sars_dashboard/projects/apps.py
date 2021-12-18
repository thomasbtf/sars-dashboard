from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    name = "sars_dashboard.projects"
    verbose_name = _("Projects")
    default_auto_field = "django.db.models.BigAutoField"
