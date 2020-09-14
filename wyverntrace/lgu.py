"""
Wyvern Trace - LGU Views

"""
import datetime
import wyvern.util.config as config

from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.views.decorators.csrf import csrf_exempt

from wyvern.util.sites import fetch_sites
from wyvern.util.chidori import wyvern_core

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyverntrace.models import WyvernTraceLog
from wyverntrace.forms import WyvernTraceLogForm

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from wyvernuser.forms import WyvernUserForm
from wyverntrace.models import WyvernMedicalForm

from wyverntrace.forms import (
    WyvernEstablishmentForm,
    WyvernEstablishmentDetailsForm,
    WyvernResidentForm,
    WyvernResidentDetailsForm,
    WyvernMedicalForms,
)

from wyverntrace.lgu import *


@wyvern_core
def view_logs(request, site=""):
    if not request.user.is_staff:
        return redirect("/")

    context = {}

    context["lgu_user"] = User.objects.get(pk=request.user.id)

    context["lgu_filter"] = context["lgu_user"].resident_establishment_filter
    context["lgu_user_ids"] = User.objects.filter(
        address__icontains=context["lgu_filter"]
    ).values("id")
    context["lgu_table_label"] = "TRACE LOCATION LOGS"
    context["lgu_logs"] = WyvernTraceLog.objects.filter(
        wyvern_user_id__in=context["lgu_user_ids"]
    ).order_by("-wyvern_trace_date")

    site_template = "themes/trace/pages/lgu/lgu-logs.html"

    return render(request, site_template, context)


@wyvern_core
def create_user(request, site=""):
    return HttpResponse("CREATE USER")


@wyvern_core
def view_users(request, type="", site=""):
    if not request.user.is_staff:
        return redirect("/")

    context = {}

    context["lgu_user"] = User.objects.get(pk=request.user.id)
    context["lgu_filter"] = context["lgu_user"].resident_establishment_filter

    context["lgu_users"] = User.objects.filter(
        address__icontains=context["lgu_filter"],
        is_location=True if type == "establishments" else False,
    ).all()

    context["lgu_table_label"] = "TRACE USERS ({})".format(type)

    site_template = "themes/trace/pages/lgu/lgu-users.html"

    return render(request, site_template, context)


@wyvern_core
def view_user(request, uuid="", site=""):
    if not request.user.is_staff:
        return redirect("/")

    context = {}

    context["lgu_user"] = User.objects.get(pk=request.user.id)

    context["lgu_filter"] = context["lgu_user"].resident_establishment_filter
    context["lgu_user_ids"] = User.objects.filter(address__icontains=context["lgu_filter"]).values_list("id")

    context["lgu_user"] = User.objects.filter(uuid=uuid).first()

    """ Check if user is within sovereign area """
    # if context["lgu_user"].id not in context["lgu_user_ids"]:
    #     return HttpResponse('FORBIDDEN: YOU CANNOT ACCESS THAT USER: LGU FILTER({}) - {} not in '.format(context["lgu_filter"], context["lgu_user"].id, context["lgu_user_ids"]))

    context["lgu_user_form"] = WyvernUserForm(request.POST, instance=context["lgu_user"])

    if request.POST and context["lgu_user_form"].is_valid():
        content["lgu_user_form"].save()

    context["lgu_table_label"] = "USER LOCATION LOGS"

    if context["lgu_user"].is_location:
        context["lgu_user_logs"] = WyvernTraceLog.objects.filter(
            wyvern_location=context["lgu_user"]
        ).all()
    else:
        context["lgu_health_declaration_forms"] = WyvernMedicalForm.objects.filter(
            wyvern_medical_form_user=context["lgu_user"]
        ).all()
        context["lgu_user_logs"] = WyvernTraceLog.objects.filter(
            wyvern_user=context["lgu_user"]
        ).all()

    context["type"] = "establishment" if context["lgu_user"].is_location else "resident"

    site_template = "themes/trace/pages/lgu/lgu-user.html"

    return render(request, site_template, context)


@wyvern_core
def view_map(request, site=""):
    return HttpResponse("TO ENABLE MAP VIEW PLEASE CONTACT info@bantay.digital")


@wyvern_core
def print_user(request, uuid="", site=""):
    return HttpResponse("PRINT USER")


@wyvern_core
def view_details(request, site=""):
    return HttpResponse("EDIT LGU DETAILS")


""" End wyverntrace/lgu.py """
