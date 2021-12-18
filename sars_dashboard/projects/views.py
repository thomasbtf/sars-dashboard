from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from sars_dashboard.projects.models import Project


# Create your views here.
class ReportListView(ListView):
    model = Project
    paginate_by = 100  # if pagination is desired


class ReportCreateView(CreateView):
    model = Project
    fields = ["title", "description"]

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"pk": self.object.pk})


class ReportDetailView(DetailView):
    model = Project


class ReportUpdateView(UpdateView):
    model = Project
    fields = ["title", "description"]
    template_name_suffix = "_update_form"


class ReportDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list")
