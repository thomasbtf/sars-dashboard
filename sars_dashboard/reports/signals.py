from django.db.models.signals import post_save
from django.dispatch import receiver

from sars_dashboard.reports.tasks import shared_unzip_report

from .models import Report


@receiver(post_save, sender=Report)
def unzip_report(sender, instance, created, **kwargs):
    if created:
        shared_unzip_report.delay(instance.pk)
