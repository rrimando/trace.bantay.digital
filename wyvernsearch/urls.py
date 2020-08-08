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
    # Search
    path("", views.index, name="search-index"),
]
