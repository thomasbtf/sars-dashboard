from rest_framework import serializers

from ..models import PangolinCall


# Serializers define the API representation.
class PangolinCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PangolinCall
        fields = "__all__"
