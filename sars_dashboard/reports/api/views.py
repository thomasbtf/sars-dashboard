from rest_framework.viewsets import ModelViewSet

from sars_dashboard.reports.models import Report

from .serializers import ReportSerializer


# ViewSets define the view behavior.
class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
