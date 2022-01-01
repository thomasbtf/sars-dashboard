from rest_framework import serializers

from ..models import Sample


# Serializers define the API representation.
class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ("__all__")
