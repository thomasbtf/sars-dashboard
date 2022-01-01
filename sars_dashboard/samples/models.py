from django.db import models

from sars_dashboard.projects.models import Project
from django.utils.translation import gettext_lazy as _

class Sample(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="samples",
        verbose_name=_("Sample"),)
    name = models.CharField(max_length=200, unique=True)
    date = models.DateField()
    date_modified = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
