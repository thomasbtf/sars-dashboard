from django.contrib import admin

from .models import ReportFiles, ReportIndex, ZippedReport

admin.site.register(ZippedReport)
admin.site.register(ReportFiles)
admin.site.register(ReportIndex)
