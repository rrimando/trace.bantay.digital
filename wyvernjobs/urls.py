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
    # Jobs
    path("", views.index, name="job-index"),
    url(r"^list/$", views.index, name="jobs-index"),
    url(r"^create/(?P<site>[-\w\d@\.-:]+)$", views.job_create, name="job-create"),
    url(r"^edit/(?P<slug>[\w.-]+)/$", views.job_edit, name="job-edit"),
    url(r"^view/(?P<slug>[\w.-]+)/$", views.job_view, name="job-view"),
    url(r"^delete/(?P<slug>[\w.-]+)/$", views.job_delete, name="job-delete"),
    url(r"^(?P<slug>[\w.-]+)/$", views.job_view, name="job-view"),
    # Job Applicants
    path("applicants/<int:pk>", views.applicant_list, name="applicant-list"),
    # Job Applications
    path("application", views.application_index, name="application-index"),
    url(r"^application/list/$", views.application_index, name="application-index"),
    url(
        r"^application/create/(?P<site>[-\w\d@\.-:]+)$",
        views.application_create,
        name="application-create",
    ),
    url(
        r"^application/edit/(?P<slug>[\w.-]+)/$",
        views.application_edit,
        name="application-edit",
    ),
    url(
        r"^application/view/(?P<slug>[\w.-]+)/$",
        views.application_view,
        name="application-view",
    ),
    url(
        r"^application/delete/(?P<slug>[\w.-]+)/$",
        views.application_delete,
        name="application-delete",
    ),
    # Jobs Categories
    # Employers and Companies
]
