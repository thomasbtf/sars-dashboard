import datetime
import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from sars_dashboard.projects.models import Project


def get_report_path(instance, filename):
    path = "report-files/{report_name}/".format(
        report_name=instance.zipped_report.zip_file.name.removesuffix(".zip")
    )
    return os.path.join(path, filename)


class Report(models.Model):
    belongs_to = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="reports",
        verbose_name=_("Project"),
    )
    date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.CharField(max_length=255, blank=True)
    zip_file = models.FileField(upload_to="report-zipped")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.zip_file.name.removesuffix(".zip")


class ReportFiles(models.Model):
    zipped_report = models.OneToOneField(Report, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)
    is_index = models.BooleanField(default=False)

    def __str__(self):
        return self.original_name


class ReportIndex(models.Model):
    zipped_report = models.OneToOneField(Report, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.original_name
