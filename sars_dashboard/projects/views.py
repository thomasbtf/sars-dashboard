from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from sars_dashboard.mixins import AdminOrStaffRequiredMixin
from sars_dashboard.projects.models import Project


# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    paginate_by = 100  # if pagination is desired


class ProjectCreateView(AdminOrStaffRequiredMixin, CreateView):
    model = Project
    fields = ["title", "description"]

    def get_success_url(self):
        return reverse("projects:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectUpdateView(AdminOrStaffRequiredMixin, UpdateView):
    model = Project
    fields = ["title", "description"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("projects:detail", kwargs={"pk": self.object.pk})


class ProjectDeleteView(AdminOrStaffRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list")
