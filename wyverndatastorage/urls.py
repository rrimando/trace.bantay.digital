"""
Wyvern Data Store - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Data Store
    path("store", views.data_store_create, name="data-store"),
    path("retrieve", views.data_store_retrieve, name="data-retrieve"),
]
