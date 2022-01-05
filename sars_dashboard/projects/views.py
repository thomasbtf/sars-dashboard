from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from guardian.shortcuts import assign_perm, remove_perm

from sars_dashboard.mixins import AdminOrStaffRequiredMixin
from sars_dashboard.projects.models import Project
from sars_dashboard.users.models import User

from .forms import AddPermissionForm, RemovePermissionForm


# Create your views here.
class ProjectListView(LoginRequiredMixin, PermissionListMixin, ListView):
    model = Project
    paginate_by = 100  # if pagination is desired
    permission_required = "projects.view_project"


class ProjectCreateView(AdminOrStaffRequiredMixin, CreateView):
    model = Project
    fields = ["title", "description"]

    def get_success_url(self):
        return reverse("projects:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Project
    permission_required = "projects.view_project"
    raise_exception = True


class ProjectUpdateView(AdminOrStaffRequiredMixin, UpdateView):
    model = Project
    fields = ["title", "description"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("projects:detail", kwargs={"pk": self.object.pk})


class ProjectDeleteView(AdminOrStaffRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list")


@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff, redirect_field_name="home")
def add_permission(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = AddPermissionForm(data=request.POST or None, project_id=project.pk)
        if form.is_valid():
            user = form.cleaned_data.get("user")

            assign_perm("view_project", user, project)

            return HttpResponseRedirect(reverse("projects:list"))

    form = AddPermissionForm(
        project_id=project.pk,
        initial={
            "user": User.objects.all()
            .exclude(is_superuser=True)
            .exclude(is_staff=True)
            .exclude(id=User.get_anonymous().pk)
            .first(),
        },
    )

    return render(
        request,
        "projects/project_add_permssion_form.html",
        {"form": form, "project": project},
    )


@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff, redirect_field_name="home")
def remove_permission(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = RemovePermissionForm(data=request.POST or None, project_id=project.pk)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            remove_perm("view_project", user, project)
            return HttpResponseRedirect(reverse("projects:list"))

    form = RemovePermissionForm(project_id=project.pk)

    return render(
        request,
        "projects/project_remove_permssion_form.html",
        {"form": form, "project": project},
    )
