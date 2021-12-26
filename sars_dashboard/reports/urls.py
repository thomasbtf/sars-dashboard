from django.urls import path

from sars_dashboard.reports.views import Report_create_view, ReportListView, ReportView

app_name = "reports"
urlpatterns = [
    path("", ReportListView.as_view(), name="list"),
    path("upload/", view=Report_create_view, name="create"),
    path("report/<int:pk>", ReportView.as_view(), name="detail"),
]
