from django.urls.base import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from sars_dashboard.mixins import AdminOrStaffRequiredMixin

from .models import Report


class ReportCreateView(AdminOrStaffRequiredMixin, CreateView):
    model = Report
    fields = "__all__"

    def get_success_url(self):
        return reverse("projects:list")


class ReportListView(AdminOrStaffRequiredMixin, ListView):
    model = Report
    paginate_by = 100  # if pagination is desired
