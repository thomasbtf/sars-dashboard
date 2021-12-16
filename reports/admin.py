from django.contrib import admin

from .models import (
    ModifedReportIndex,
    ReportFiles,
    ReportIndex,
    ReportRawData,
    ReportThumbnails,
    ZippedReport,
)

admin.site.register(ZippedReport)
admin.site.register(ReportFiles)
admin.site.register(ModifedReportIndex)
admin.site.register(ReportIndex)
admin.site.register(ReportRawData)
admin.site.register(ReportThumbnails)
