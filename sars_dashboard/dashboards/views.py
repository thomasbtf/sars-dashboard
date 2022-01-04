import pandas as pd
import plotly.express as px
from django.views.generic.base import TemplateView
from plotly.offline import plot

from sars_dashboard import projects, samples
from sars_dashboard.calls.models import PangolinCall
from sars_dashboard.projects import context_processors
from sars_dashboard.projects.models import Project
from sars_dashboard.samples.models import Sample
from sars_dashboard.voc_definitions import VOCS


class SarsDashboardView(TemplateView):
    template_name = "dashboards/sars-cov-2-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        no_data = "No data."

        first_project = Project.objects.first()
        if first_project is None:
            context["project_name"] = "No project found"

        samples_of_project = Sample.objects.filter(project=first_project)

        if not samples_of_project.exists():
            context["processed_samples"] = "-"
        else:
            context["processed_samples"] = samples_of_project.count()

        calls_of_project = PangolinCall.objects.filter(sample__in=samples_of_project)
        if not calls_of_project.exists():
            context["over_time_plot"] = no_data
            context["table"] = no_data
            context["unique_calls"] = "-"
        else:
            calls_all_data = self.extract_and_mask_lineages_per_day(calls_of_project)
            context["over_time_plot"] = self.plot_lineages_over_time(calls_all_data)
            context["table"] = self.get_table_of_lineages(calls_all_data)
            context["unique_calls"] = calls_of_project.count()

        latest_run_date = samples_of_project.order_by("-date").first()

        if latest_run_date is None:
            context["latest_run_plot"] = no_data
            context["last_update"] = "-"
        else:
            samples_of_latest_run = samples_of_project.filter(date=latest_run_date.date)
            calls_of_last_run = PangolinCall.objects.filter(
                sample__in=samples_of_latest_run
            )
            lineages_of_last_run = self.extract_and_mask_lineages_per_day(
                calls_of_last_run
            )
            context["latest_run_plot"] = self.plot_lineages_of_last_run(
                lineages_of_last_run
            )
            context["last_update"] = latest_run_date.date

        return context

    def get_table_of_lineages(self, table):
        """Creates a table of the lineages in the last run"""

        table["Week"] = pd.to_datetime(table["Date"]).dt.strftime("%W")
        table["Year"] = pd.to_datetime(table["Date"]).dt.strftime("%Y")
        table = table.groupby(["Year", "Week", "Lineage"]).sum().reset_index()

        if len(table) == 0:
            return pd.DataFrame(columns=["Year", "Week", "Lineage", "# of Lineages"])

        table = (
            table.pivot(
                index=["Year", "Week"], columns="Lineage", values="# of Lineages"
            )
            .fillna(0.0)
            .reset_index()
        )
        table = table.astype(int)

        table = table.to_html(
            classes='table table-bordered dataTable" id="dataTable" width="100%" cellspacing="0" role="grid" style="width: 100%;',
            index=False,
            index_names=False,
            justify="center",
            border=0,
        )
        return table

    def plot_lineages_of_last_run(self, data):
        """Created a plot of the lineages of the last run as a doughnut chart"""

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

    def plot_lineages_over_time(self, data):
        """Created a plot of the lineages over time as a bar chart"""

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
        """Extracts the lineages per day from given calls and masks the lineages that are not in the list of VOCs"""

        all_lineages = []
        for call in calls:
            all_lineages.append(
                {
                    "Called Lineage": call.lineage,
                    "Date": call.sample.date,
                }
            )
        all_lineages = pd.DataFrame(all_lineages)

        if len(all_lineages) == 0:
            return pd.DataFrame(columns=["Date", "Lineage", "# of Lineages"])

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
