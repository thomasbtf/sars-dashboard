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

        # with zipfile.ZipFile(instance.zip_file, "r") as zipped_report:
        #     for i, name in enumerate(zipped_report.namelist()):

        #         if os.path.join("data", "raw") in name:
        #             # if the file is a raw file
        #             _, new_name = name.split(os.path.join("data", "raw/"), 1)
        #             file = ContentFile(zipped_report.read(name), name=new_name)
        #             ReportRawData.objects.create(zipped_report=instance, file=file, original_name=name)

        #         elif os.path.join("data", "thumbnails") in name:
        #             # if the file is a thumbnail
        #             _, new_name = name.split(os.path.join("data", "thumbnails/"), 1)
        #             file = ContentFile(zipped_report.read(name), name=new_name)
        #             ReportThumbnails.objects.create(zipped_report=instance, file=file, original_name=name)

        #         elif name.endswith('report.html') and name.count("/") == 1:
        #             # if the file is the index
        #             file = ContentFile(zipped_report.read(name), name=name)
        #             ReportIndex.objects.create(zipped_report=instance, file=file, original_name=name)

        # assert instance.reportindex_set.count() == 1

        # mod_file = ContentFile(instance.reportindex_set.first().file.read(), name=f"{report_name}-index.html")
        # modifed_index = ModifedReportIndex.objects.create(zipped_report=instance, file=mod_file)

        # Read in the modifed index
        # with modifed_index.file.open("r") as file:
        #     filedata = file.read()

        # raw_files = ReportRawData.objects.filter(zipped_report=instance)
        # print(raw_files)
        # # Replace the target string
        # for report_file in raw_files:
        #     new = report_file.file.url.removeprefix(settings.MEDIA_URL)
        #     new = re.sub(r'report-files\/\d{4}\/\d{2}\/\d{2}\/', ' ', new)
        #     original = re.sub(r"^.*?\/", "", report_file.original_name)
        #     print("original name:", original)
        #     print("new name:", new)
        #     print()
        #     filedata = filedata.replace(original, new)

        # # Write the file out again
        # with modifed_index.file.open("w") as file:
        #     file.write("I was here")
        #     file.write(filedata)

        #     for i, name in enumerate(zipped_report.namelist()):
        #         suffix = Path(name).suffix
        #         is_index = name.endswith('report.html') and name.count("/") == 1
        #         if is_index:
        #             print(name)
        #         storage_filename = f'{report_name}-{i}{suffix}'
        #         file = ContentFile(zipped_report.read(name), name=storage_filename)
        #         ReportFiles.objects.create(zipped_report=instance, original_name=name, file=file, is_index=is_index)

        # # modify the report index file
        # index_file = ReportFiles.objects.filter(zipped_report=instance, is_index=True)
        # assert len(index_file) == 1
        # index_file = index_file[0]

        # mod_file = ContentFile(index_file.file.read(), name=f"{report_name}-index.html")
        # modifed_index = ModifedReportIndex.objects.create(zipped_report=instance, file=mod_file)

        # report_files = ReportFiles.objects.filter(zipped_report=instance, is_index=False)

        # # Read in the file
        # with modifed_index.file.open("r") as file:
        #     filedata = file.read()

        # media_url = settings.MEDIA_URL
        # # Replace the target string
        # for report_file in report_files:
        #     new = report_file.file.url.removeprefix(media_url)
        #     new = re.sub(r'report-files\/\d{4}\/\d{2}\/\d{2}\/', ' ', new)
        #     original = re.sub(r"^.*?\/", "", report_file.original_name)
        #     print("original name:", original)
        #     print("new name:", new)
        #     print()
        #     filedata = filedata.replace(original, new)

        # # Write the file out again
        # with modifed_index.file.open("w") as file:
        #     file.write("I was here")
        #     file.write(filedata)
