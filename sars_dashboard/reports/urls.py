from django.urls import path, re_path

from sars_dashboard.reports.views import (
    ReportCreateView,
    ReportListView,
    download_zip_file,
    view_data,
    view_index,
)

app_name = "reports"
urlpatterns = [
    path("", ReportListView.as_view(), name="list"),
    path("upload/", view=ReportCreateView.as_view(), name="create"),
    path("<int:report_pk>/download", view=download_zip_file, name="download"),
    path("<int:report_pk>/view", view=view_index, name="view"),
    re_path(r"(?P<report_pk>\d+)/data/(?P<path>.+)", view=view_data, name="data"),
]
