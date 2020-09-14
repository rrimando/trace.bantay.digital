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
    # Registration
    path("register/<str:type>/", views.register, name="trace-register-user"),
    # User Dashboard
    path("dashboard/", views.dashboard, name="trace-dashboard-user"),
    # API END POINTS
    # TODO: MOVE TO DRF
    # Fetch User Details
    path("fetch/<str:uuid>/", views.fetch, name="trace-fetch-user"),
    # Log User Location
    path("log/<str:uuid>/", views.log, name="trace-log-user"),

    # LGU Views
    path("lgu/logs/", views.view_logs, name="trace-lgu-logs"),
    path("lgu/register/", views.create_user, name="trace-lgu-register"),
    path("lgu/view/<str:type>", views.view_users, name="trace-lgu-view-users"),
    path("lgu/user/<str:uuid>", views.view_user, name="trace-lgu-view-user"),
    path("lgu/print/<str:uuid>", views.print_user, name="trace-lgu-print-user"),
    path("lgu/map/", views.view_map, name="trace-lgu-map"),
    path("lgu/details/", views.view_details, name="trace-lgu-details"),
]
