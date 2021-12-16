from django.urls import path

from reports.views import ZippedReport_create_view

app_name = "reports"
urlpatterns = [
    path("upload/", view=ZippedReport_create_view, name="redirect"),
]
