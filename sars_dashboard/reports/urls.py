from django.urls import path

from sars_dashboard.reports.views import ReportCreateView, ReportListView

app_name = "reports"
urlpatterns = [
    path("", ReportListView.as_view(), name="list"),
    path("upload/", view=ReportCreateView.as_view(), name="create"),
]
