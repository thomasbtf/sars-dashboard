from guardian.shortcuts import get_objects_for_user


def projects(request):
    user = request.user
    projects = get_objects_for_user(user, "projects.view_project")
    return {"projects_context": projects}
