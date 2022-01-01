from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from sars_dashboard.samples.models import Sample


# Create your views here.
class SampleListView(ListView):
    model = Sample
    paginate_by = 100  # if pagination is desired


class SampleCreateView(CreateView):
    model = Sample
    fields = ("__all__")

    def get_success_url(self):
        return reverse("samples:detail", kwargs={"pk": self.object.pk})


class SampleDetailView(DetailView):
    model = Sample


class SampleUpdateView(UpdateView):
    model = Sample
    fields = ("__all__")
    template_name_suffix = "_update_form"


class SampleDeleteView(DeleteView):
    model = Sample
    success_url = reverse_lazy("samples:list")
