from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from sars_dashboard.changelog.views import ChangelogView
from sars_dashboard.dashboards.views import SarsDashboardView

urlpatterns = [
    path("", SarsDashboardView.as_view(), name="home"),
    path("run/", TemplateView.as_view(template_name="pages/run.html"), name="run"),
    path(
        "contact/",
        TemplateView.as_view(template_name="pages/contact.html"),
        name="contact",
    ),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path("changelog/", ChangelogView.as_view(), name="changelog"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("sars_dashboard.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("project/", include("sars_dashboard.projects.urls", namespace="projects")),
    path("report/", include("sars_dashboard.reports.urls", namespace="reports")),
    path("sample/", include("sars_dashboard.samples.urls", namespace="samples")),
    path("calls/", include("sars_dashboard.calls.urls", namespace="calls")),
]

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
