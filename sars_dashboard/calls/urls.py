from django.urls import path

from sars_dashboard.calls.views import (
    PangolinCallCreateView,
    PangolinCallDeleteView,
    PangolinCallDetailView,
    PangolinCallListView,
    PangolinCallUpdateView,
)

app_name = "calls"
urlpatterns = [
    path("", PangolinCallListView.as_view(), name="list"),
    path("pango/", PangolinCallListView.as_view(), name="pango-list"),
    path("pango/<int:pk>", PangolinCallDetailView.as_view(), name="pango-detail"),
    path("pango/update/<int:pk>", PangolinCallUpdateView.as_view(), name="pango-update"),
    path("pango/delete/<int:pk>", PangolinCallDeleteView.as_view(), name="pango-delete"),
    path("pango/create/", PangolinCallCreateView.as_view(), name="pango-create"),
]
