from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sars_dashboard.calls.api.views import PangolinCallViewSet
from sars_dashboard.reports.api.views import ReportViewSet
from sars_dashboard.samples.api.views import SampleViewSet
from sars_dashboard.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("report", ReportViewSet)
router.register("call/lineage", PangolinCallViewSet)
router.register("sample", SampleViewSet)


app_name = "api"
urlpatterns = router.urls
