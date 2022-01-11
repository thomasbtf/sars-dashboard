import os

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django_sendfile import sendfile

from sars_dashboard.mixins import AdminOrStaffRequiredMixin

from .models import Report, ReportIndex


class ReportCreateView(AdminOrStaffRequiredMixin, CreateView):
    model = Report
    fields = "__all__"

    def get_success_url(self):
        return reverse("projects:list")


class ReportListView(AdminOrStaffRequiredMixin, ListView):
    model = Report
    paginate_by = 100  # if pagination is desired


def download_zip_file(request, report_pk):
    report = get_object_or_404(Report, pk=report_pk)
    return _auth_view(request, report_pk, report.zip_file.path)


def view_index(request, report_pk):
    report_index = get_object_or_404(ReportIndex, zipped_report=report_pk)
    return _auth_view(request, report_pk, report_index.file.path)


def view_data(request, report_pk, path):
    report_index = get_object_or_404(ReportIndex, zipped_report=report_pk)
    path = os.path.join(
        report_index.file.path.removesuffix("report.html"), "data", path
    )
    return _auth_view(request, report_pk, path)


@login_required
def _auth_view(request, report_pk, path):
    report = get_object_or_404(Report, pk=report_pk)
    project = report.belongs_to
    user = request.user

    if (
        user.has_perm("projects.view_project", project)
        or user.is_staff
        or user.is_superuser
    ):
        return sendfile(request, path)

    return HttpResponseNotFound()
