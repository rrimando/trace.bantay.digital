""" 
Wyvern LMS - URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from wyvernlms import views

urlpatterns = [
    url(r"", views.index, name="lms-index"),
    url(r"^enroll/$", views.enroll, name="lms-enroll"),
]
