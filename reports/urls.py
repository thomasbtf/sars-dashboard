from django.urls import path

from reports.views import Report_create_view, ReportListView, ReportView

app_name = "reports"
urlpatterns = [
    path("", ReportListView.as_view(), name="report-list"),
    path("upload/", view=Report_create_view, name="redirect"),
    path("report/<int:pk>", ReportView.as_view(), name="report-detail"),
]
