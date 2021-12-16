from django.contrib import admin

from .models import Report, ReportFiles, ReportIndex

admin.site.register(Report)
admin.site.register(ReportFiles)
admin.site.register(ReportIndex)
