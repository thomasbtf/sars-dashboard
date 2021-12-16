import os

from django.db import models


def get_report_raw_path(instance, filename):
    path = "report-files/{report_name}/data/raw".format(
        report_name=instance.zipped_report.zip_file.name.removesuffix(".zip")
    )
    return os.path.join(path, filename)


def get_report_thumpnail_path(instance, filename):
    path = "report-files/{report_name}/data/thumbnails".format(
        report_name=instance.zipped_report.zip_file.name.removesuffix(".zip")
    )
    return os.path.join(path, filename)


def get_report_index_path(instance, filename):
    path = "report-files/{report_name}/".format(
        report_name=instance.zipped_report.zip_file.name.removesuffix(".zip")
    )
    return os.path.join(path, filename)


def get_report_mod_index_path(instance, filename):
    path = "report-files/{report_name}/".format(
        report_name=instance.zipped_report.zip_file.name.removesuffix(".zip")
    )
    return os.path.join(path, filename)


def get_report_file_path(instance, filename):
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
    file = models.FileField(upload_to=get_report_file_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)
    is_index = models.BooleanField(default=False)


class ReportRawData(models.Model):
    zipped_report = models.ForeignKey(ZippedReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_raw_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)


class ReportThumbnails(models.Model):
    zipped_report = models.ForeignKey(ZippedReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_thumpnail_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)


class ReportIndex(models.Model):
    zipped_report = models.ForeignKey(ZippedReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_index_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)


class ModifedReportIndex(models.Model):
    zipped_report = models.ForeignKey(ZippedReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_report_mod_index_path, max_length=255)
    original_name = models.CharField(max_length=255, blank=True)
