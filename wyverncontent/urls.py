"""

Wyvern Shop - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(
        r"^fetch/(?P<slug>[-\w\d@\.-:]+)/(?P<site>[-\w\d@\.-:]+)/$",
        views.fetch,
        name="application-create",
    ),
    url(
        r"^update/(?P<slug>[\w.-]+)/(?P<site>[-\w\d@\.-:]+)/$",
        views.update,
        name="application-edit",
    ),
]
