from django.urls import path

from sars_dashboard.samples.views import (
    SampleCreateView,
    SampleDeleteView,
    SampleDetailView,
    SampleListView,
    SampleUpdateView,
)

app_name = "samples"
urlpatterns = [
    path("", SampleListView.as_view(), name="list"),
    path("<int:pk>", SampleDetailView.as_view(), name="detail"),
    path("update/<int:pk>", SampleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", SampleDeleteView.as_view(), name="delete"),
    path("create/", SampleCreateView.as_view(), name="create"),
]
