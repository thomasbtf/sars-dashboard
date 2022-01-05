from django.urls import path

from sars_dashboard.projects.views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("<int:pk>", ProjectDetailView.as_view(), name="detail"),
    path("update/<int:pk>", ProjectUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ProjectDeleteView.as_view(), name="delete"),
    path("create/", ProjectCreateView.as_view(), name="create"),
]
