from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Project

# Register your models here.
# admin.site.register(Project)


class ProjectAdmin(GuardedModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
