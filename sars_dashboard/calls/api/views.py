from rest_framework.viewsets import ModelViewSet

from sars_dashboard.calls.models import PangolinCall

from .serializers import PangolinCallSerializer


# ViewSets define the view behavior.
class PangolinCallViewSet(ModelViewSet):
    queryset = PangolinCall.objects.all()
    serializer_class = PangolinCallSerializer
