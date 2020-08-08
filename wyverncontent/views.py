"""
Wyvern Custom Content - Endpoints
TODO: Consider putting this into the API

"""
from django.urls import reverse

from rest_framework import serializers
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from wyvern.util.chidori import wyvern_core

from django import template

from wyverncontent.models import WyvernSite
from wyverncontent.models import WyvernCustomContent


@wyvern_core
def fetch(request, slug="", site=""):

    site = WyvernSite.objects.filter(site_url=site).get()
    custom_content = WyvernCustomContent.objects.filter(
        wyvern_custom_content_site=site, wyvern_custom_content_slug=slug
    ).get()

    title = (
        custom_content.wyvern_custom_content_label
        if custom_content.wyvern_custom_content_label
        else (custom_content.wyvern_custom_content_slug).replace("_", " ").title()
    )

    return JsonResponse(
        {"title": title, "content": custom_content.wyvern_custom_content_content}
    )


@wyvern_core
@method_decorator(csrf_exempt, name="dispatch")
def update(request, slug="", site=""):

    site = WyvernSite.objects.filter(site_url=site).get()
    custom_content = WyvernCustomContent.objects.filter(
        wyvern_custom_content_site=site, wyvern_custom_content_slug=slug
    ).get()

    custom_content.wyvern_custom_content_content = request.POST.get(
        "wyvern_custom_content_content"
    )
    custom_content.save()

    return JsonResponse({"success": "true"})


@wyvern_core
def upload(request, slug="", site=""):
    pass


"""EOF"""
