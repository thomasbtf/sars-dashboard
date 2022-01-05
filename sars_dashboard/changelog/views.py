import markdown
from django.views.generic.base import TemplateView


class ChangelogView(TemplateView):
    template_name = "pages/changelog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open("CHANGELOG.md", "r", encoding="utf-8") as input_file:
            text = input_file.read()
        html = markdown.markdown(text)

        context["changelog"] = html

        return context
