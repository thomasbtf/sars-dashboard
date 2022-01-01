from sars_dashboard.calls.models import PangolinCall


def count_pango_calls(request):
    return {
        "unique_pangolin_calls": PangolinCall.objects.values("lineage")
        .distinct()
        .count()
    }
