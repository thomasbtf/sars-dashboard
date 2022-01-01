from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from sars_dashboard.calls.models import PangolinCall


# Create your views here.
class PangolinCallListView(ListView):
    model = PangolinCall
    paginate_by = 100  # if pagination is desired


class PangolinCallCreateView(CreateView):
    model = PangolinCall
    fields = "__all__"

    def get_success_url(self):
        return reverse("calls:pango-detail", kwargs={"pk": self.object.pk})


class PangolinCallDetailView(DetailView):
    model = PangolinCall


class PangolinCallUpdateView(UpdateView):
    model = PangolinCall
    fields = "__all__"
    template_name_suffix = "_update_form"


class PangolinCallDeleteView(DeleteView):
    model = PangolinCall
    success_url = reverse_lazy("calls:list")
