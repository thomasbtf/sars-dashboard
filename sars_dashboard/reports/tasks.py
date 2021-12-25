import zipfile
from pathlib import Path

from celery import shared_task
from django.core.files.base import ContentFile

from .models import Report, ReportFiles, ReportIndex


@shared_task(soft_time_limit=10000)
def shared_unzip_report(pk):
    """Unzip the report file and save the files to the database."""

    report = Report.objects.get(pk=pk)

    # unzip the report
    with zipfile.ZipFile(report.zip_file, "r") as zipped_report:
        for name in zipped_report.namelist():

            # remove the first directory from the path
            new_name = Path(*Path(name).parts[1:])

            # if the file is the index
            if name.endswith("report.html") and name.count("/") == 1:
                file = ContentFile(zipped_report.read(name), name=new_name)
                ReportIndex.objects.create(
                    zipped_report=report, file=file, original_name=name
                )
            else:
                file = ContentFile(zipped_report.read(name), name=new_name)
                ReportFiles.objects.create(
                    zipped_report=report, file=file, original_name=name
                )
