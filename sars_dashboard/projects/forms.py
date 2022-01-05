from django import forms
from guardian.shortcuts import get_users_with_perms

from sars_dashboard.users.models import User

from .models import Project


class AddPermissionForm(forms.Form):
    def __init__(self, project_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if project_id:
            users_with_perms = get_users_with_perms(
                Project.objects.get(id=project_id)
            ).values("pk")
            all_users = (
                User.objects.all()
                .exclude(is_superuser=True)
                .exclude(is_staff=True)
                .exclude(id=User.get_anonymous().pk)
            )
            self.fields["user"].queryset = all_users.exclude(id__in=users_with_perms)

    user = forms.ModelChoiceField(queryset=None)


class RemovePermissionForm(forms.Form):
    def __init__(self, project_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if project_id:
            self.fields["user"].queryset = get_users_with_perms(
                Project.objects.get(id=project_id)
            )

    user = forms.ModelChoiceField(queryset=None)
