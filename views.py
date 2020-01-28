from django.apps import apps
from django.views.generic import TemplateView
import django.apps
from wagtail.core.models import Page
import inspect


class WagtailReportListingview(TemplateView):
    template_name = "wagtailreport/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report_pages = []
        apps = django.apps.apps.get_models()
        for app in apps:
            if issubclass(app, Page) and app._meta.verbose_name != 'page': #TODO, this won't hold up...
                model = {}
                model.update({'label': app._meta.verbose_name})
                # Get model counts
                model.update({'count': app.objects.all().count()})
                model.update({'details': inspect.getmro(app)})
                report_pages.append(model)

        context['report'] = report_pages

        return context