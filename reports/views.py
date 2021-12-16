from django.shortcuts import redirect, render

from .forms import ZippedReportForm


# @login_required
def ZippedReport_create_view(request):
    if request.method == "POST":
        form = ZippedReportForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = ZippedReportForm()
    return render(request, "reports/model_form_upload.html", {"form": form})
