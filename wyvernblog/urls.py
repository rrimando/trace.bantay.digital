""" 

Wyvern Blog - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from wyvernblog import views

urlpatterns = [
    url(r"^create/(?P<site>[-\w\d@\.-:]+)/$", views.create, name="blog-create"),
    url(r"^list/(?P<site>[\w\d@\.-:]+)/$", views.list, name="blog-list"),
    url(
        r"^edit/(?P<slug>[-\w]+)/(?P<site>[\w\d@\.-:]+)/$", views.edit, name="blog-edit"
    ),
    url(
        r"^view/(?P<slug>[-\w]]+)/(?P<site>[\w\d@\.-:]+)/$",
        views.view,
        name="blog-view",
    ),
    url(
        r"^delete/(?P<slug>[-\w]+)/(?P<site>[\w\d@\.-:]+)/$",
        views.delete,
        name="blog-delete",
    ),
    url(r"^(?P<site>[-\w\d@\.-:]+)/$", views.index, name="blog-index"),
    url(r"", views.index, name="blog-index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
