import pandas as pd
import plotly.express as px
from django.views.generic.base import TemplateView
from plotly.offline import plot

from sars_dashboard.calls.models import PangolinCall
from sars_dashboard.samples.models import Sample
from sars_dashboard.voc_definitions import VOCS


class SarsDashboardView(TemplateView):
    template_name = "dashboards/sars-cov-2-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["latest_run_plot"] = self.plot_lineages_of_last_run()
        context["over_time_plot"] = self.plot_lineages_over_time()

        return context

    def plot_lineages_of_last_run(self):
        # get latest run data
        latest_run_date = Sample.objects.order_by("-date").first().date
        samples = Sample.objects.filter(date=latest_run_date)
        calls = PangolinCall.objects.filter(sample__in=samples)

        data = self.extract_and_mask_lineages_per_day(calls)

        fig = px.pie(
            data,
            values="# of Lineages",
            names="Lineage",
            hover_data=["Lineage"],
            hole=0.8,
        )

        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(
            legend=dict(
                orientation="h",
            )
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )

        plot_div = plot(fig, output_type="div", include_plotlyjs=False)
        return plot_div

    def plot_lineages_over_time(self):
        calls = PangolinCall.objects.all()

        data = self.extract_and_mask_lineages_per_day(calls)

        fig = px.bar(data, x="Date", y="# of Lineages", color="Lineage")

        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )

        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", xanchor="left", y=-0.85, x=0)
        )

        fig.update_xaxes(
            rangeslider_visible=True,
        )

        plot_div = plot(fig, output_type="div", include_plotlyjs=False)
        return plot_div

    def extract_and_mask_lineages_per_day(self, calls):
        all_lineages = []
        for call in calls:
            all_lineages.append(
                {
                    "Called Lineage": call.lineage,
                    "Date": call.sample.date,
                }
            )
        all_lineages = pd.DataFrame(all_lineages)

        for masked_lineage, lineage in VOCS.items():
            all_lineages.loc[
                all_lineages["Called Lineage"].str.contains(lineage), "Lineage"
            ] = masked_lineage

        all_lineages["Lineage"] = all_lineages["Lineage"].fillna("Other")

        all_lineages = (
            all_lineages.groupby(by=["Date", "Lineage"])
            .size()
            .reset_index(name="# of Lineages")
        )

        return all_lineages
