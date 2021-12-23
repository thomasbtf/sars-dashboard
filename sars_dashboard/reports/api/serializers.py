from rest_framework import serializers

from ..models import Report


# Serializers define the API representation.
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("zip_file", "description")
