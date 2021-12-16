from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ReportForm
from .models import Report


# @login_required
def Report_create_view(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = ReportForm()
    return render(request, "reports/model_form_upload.html", {"form": form})


class ReportListView(ListView):
    model = Report
    paginate_by = 100  # if pagination is desired


class ReportView(DetailView):
    model = Report
