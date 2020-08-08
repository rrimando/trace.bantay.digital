"""

Wyvern Site - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Site View
    path("", views.index, name="site-index"),
    url(r"^preview/$", views.index),
    url(r"^create/$", views.create, name="site-create"),
    url(r"^preview/(?P<site>[-\w\d@\.-:]+)/$", views.index, name="site-preview"),
    url(
        r"^configure/(?P<site>[-\w\d@\.-:]+)/$", views.configure, name="site-configure"
    ),
    url(r"^manage/(?P<site>[-\w\d@\.-:]+)/$", views.manage, name="site-manage"),
    url(r"^delete/(?P<site>[-\w\d@\.-:]+)/$", views.delete, name="site-delete"),
]
