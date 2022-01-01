from rest_framework.viewsets import ModelViewSet

from sars_dashboard.samples.models import Sample

from .serializers import SampleSerializer


# ViewSets define the view behavior.
class SampleViewSet(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    lookup_field = "name"
