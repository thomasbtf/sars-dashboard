from django import forms

from .models import ZippedReport


class ZippedReportForm(forms.ModelForm):
    class Meta:
        model = ZippedReport
        fields = (
            "description",
            "zip_file",
        )
