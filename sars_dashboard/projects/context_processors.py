from ..reports.models import Project


def projects(request):
    projects = Project.objects.all()
    return {"projects": projects}
