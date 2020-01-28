from django.apps import apps
from django.conf import settings
from django.conf.urls import url
from django.utils.safestring import mark_safe

from wagtail.core import hooks

from .views import WagtailReportListingview


@hooks.register('register_admin_urls')
def urlconf_time():
    return [
        url(r'^wagtailreport/',
            WagtailReportListingview.as_view()),
    ]

