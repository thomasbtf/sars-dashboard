from django.db import models
from django.utils.translation import gettext_lazy as _

from sars_dashboard.samples.models import Sample


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"min_value": self.min_value, "max_value": self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Call(models.Model):
    sample = models.ForeignKey(
        Sample,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="calls",
        verbose_name=_("Call"),
    )
    date_modified = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PangolinCall(Call):
    taxon = models.CharField(max_length=100)
    lineage = models.CharField(max_length=100)
    conflict = models.CharField(max_length=100)
    ambiguity_score = MinMaxFloat(min_value=0.0, max_value=1.0)
    scorpio_call = models.CharField(max_length=100)
    scorpio_support = MinMaxFloat(min_value=0.0, max_value=1.0)
    scorpio_conflict = MinMaxFloat(min_value=0.0, max_value=1.0)
    version = models.CharField(max_length=100)
    pangolin_version = models.CharField(max_length=100)
    pangoLEARN_version = models.CharField(max_length=100)
    pango_version = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.lineage
