from django.urls import path

from sars_dashboard.projects.views import (
    ReportCreateView,
    ReportDeleteView,
    ReportDetailView,
    ReportListView,
    ReportUpdateView,
)

app_name = "projects"
urlpatterns = [
    path("", ReportListView.as_view(), name="list"),
    path("<int:pk>", ReportDetailView.as_view(), name="detail"),
    path("update/<int:pk>", ReportUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ReportDeleteView.as_view(), name="delete"),
    path("create/", ReportCreateView.as_view(), name="create"),
]
