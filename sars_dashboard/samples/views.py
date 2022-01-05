from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from sars_dashboard.mixins import AdminOrStaffRequiredMixin
from sars_dashboard.samples.models import Sample


# Create your views here.
class SampleListView(AdminOrStaffRequiredMixin, ListView):
    model = Sample
    paginate_by = 100  # if pagination is desired


class SampleCreateView(AdminOrStaffRequiredMixin, CreateView):
    model = Sample
    fields = "__all__"

    def get_success_url(self):
        return reverse("samples:detail", kwargs={"pk": self.object.pk})


class SampleDetailView(AdminOrStaffRequiredMixin, DetailView):
    model = Sample


class SampleUpdateView(AdminOrStaffRequiredMixin, UpdateView):
    model = Sample
    fields = "__all__"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("samples:detail", kwargs={"pk": self.object.pk})


class SampleDeleteView(AdminOrStaffRequiredMixin, DeleteView):
    model = Sample
    success_url = reverse_lazy("samples:list")
