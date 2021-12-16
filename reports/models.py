import os

from django.db import models


def get_report_path(instance, filename):
    path = "report-files/{report_name}/".format(
        report_name=instance.zipped_report.zip_file.name.removesuffix(".zip")
    )
    return os.path.join(path, filename)


class ZippedReport(models.Model):
    description = models.CharField(max_length=255, blank=True)
    zip_file = models.FileField(upload_to="reports-zipped")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ReportFiles(models.Model):
    zipped_report = models.ForeignKey(ZippedReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)
    is_index = models.BooleanField(default=False)


class ReportIndex(models.Model):
    zipped_report = models.ForeignKey(ZippedReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)
