import zipfile
from pathlib import Path

from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ReportFiles, ReportIndex, ZippedReport


@receiver(post_save, sender=ZippedReport)
def unzip_report(sender, instance, created, **kwargs):
    if created:
        # unzip the report
        with zipfile.ZipFile(instance.zip_file, "r") as zipped_report:
            for i, name in enumerate(zipped_report.namelist()):

                # remove the first directory from the path
                new_name = Path(*Path(name).parts[1:])

                # if the file is the index
                if name.endswith("report.html") and name.count("/") == 1:
                    print(name)
                    print(new_name)
                    print()
                    file = ContentFile(zipped_report.read(name), name=new_name)
                    ReportIndex.objects.create(
                        zipped_report=instance, file=file, original_name=name
                    )
                else:
                    print(name)
                    print(new_name)
                    print()
                    file = ContentFile(zipped_report.read(name), name=new_name)
                    ReportFiles.objects.create(
                        zipped_report=instance, file=file, original_name=name
                    )
