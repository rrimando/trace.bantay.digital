""" 
Wyvern Trace - URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from wyverntrace import views

urlpatterns = [
    path("", views.index, name="trace-index"),
    path("map/", views.map, name="trace-map"),
    path("generated/", views.generated, name="trace-generated"),
    # Fetch User Details
    url(r"^fetch/(?P<user_id>[-\d]+)/$", views.fetch, name="trace-fetch-user"),
    # Log User Location
    url(r"^log/(?P<user_id>[-\d]+)/$", views.log, name="trace-log-user"),
]