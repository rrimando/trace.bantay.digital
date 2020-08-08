from django.urls import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core

from django import template

from wyvernsite.models import WyvernSite
from wyverndatastorage.models import WyvernDataStore


@wyvern_core
def data_store_create(request, site=""):
    return HttpResponse("")


@wyvern_core
def data_store_retrieve(request, site=""):
    return HttpResponse("")
