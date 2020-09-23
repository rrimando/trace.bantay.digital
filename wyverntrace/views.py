"""
Wyvern Trace - Views

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
def index(request, site=""):
    return redirect("/")


@wyvern_core
def dashboard(request):

    # Redirect User to Landing Page If Not Logged In
    if not request.user.is_authenticated:
        return redirect("/")

    if request.user.is_staff:
        return redirect(reverse("trace-lgu-logs"))

    # Fetch Initial Data From User Info in Request
    user = User.objects.get(pk=request.user.id) if (request.user.id) else None
    site = WyvernSite.objects.get(pk=request.site.id) or None

    # Prepare Context
    context = {
        "user": user,
        "site": site,
        "type": "establishment" if user.is_location else "resident",
    }

    # Load Registration Forms
    context["resident_form"] = WyvernResidentDetailsForm(
        request.POST or None,
        instance=user,
        auto_id="resident_%s",
    )

    context["establishment_form"] = WyvernEstablishmentDetailsForm(
        request.POST or None,
        instance=user,
        auto_id="establishment_%s",
    )

    if context["type"] == "establishment":
        context["manual_log"] = WyvernTraceLogForm(
            request.POST or None,
            auto_id="manual_%s",
        )

    # Prepare Resident Exclusive Content - This Prevents Creating Health Declaration Forms for None Residents
    if context["type"] == "resident":
        # Fetch Latest Medical Form
        # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get-or-create
        # https://stackoverflow.com/questions/7217811/query-datetime-by-todays-date-in-django
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        user_health_dec, created = WyvernMedicalForm.objects.get_or_create(
            wyvern_medical_form_user=user,
            wyvern_medical_form_date__range=(today_min, today_max),
        )
        context["user_health_dec"] = user_health_dec
        context["medical_form"] = WyvernMedicalForms(
            request.POST or None,
            instance=user_health_dec,  # We are pretty sure this isn't None because of get_or_create
        )
        context["today"] = datetime.date.today()

    if request.POST:
        if context["type"] == "establishment" and context["manual_log"].is_valid():
            if context["manual_log"].is_valid():
                manualLog = context["manual_log"].save(commit=False)
                manualLog.wyvern_location = request.user
                manualLog.save()
                messages.add_message(
                    request, 20, "You have successfully log a resident."
                )
            else:
                messages.add_message(
                    request, 20, "There was an error with your submission"
                )
            return redirect(reverse("trace-dashboard-user"))

        if context["type"] == "resident" and context["medical_form"].is_valid():
            if context["medical_form"].is_valid():
                context["medical_form"].save()
                messages.add_message(
                    request, 20, "Thank you for filling up your health declaration form"
                )
            else:
                messages.add_message(
                    request, 20, "There was an error with your submission"
                )
            return redirect(reverse("trace-dashboard-user"))

        if context["type"] == "resident" and context["resident_form"].is_valid():
            context["resident_form"].save()
            messages.add_message(request, 20, "Your details have been updated")
            return redirect(reverse("trace-dashboard-user"))

        if (
            context["type"] == "establishment"
            and context["establishment_form"].is_valid()
        ):
            context["establishment_form"].save()
            messages.add_message(request, 20, "Your details have been updated")
            return redirect(reverse("trace-dashboard-user"))

    if request.user.is_location:
        context["logs"] = WyvernTraceLog.objects.filter(
            wyvern_location=request.user
        ).order_by(
            "-id"
        )  # [:10]
    else:
        context["logs"] = WyvernTraceLog.objects.filter(
            wyvern_user=request.user
        ).order_by(
            "-id"
        )  # [:10]

    site_template = "themes/trace/pages/dashboard.html"
    return render(request, site_template, context)


@wyvern_core
def register(request, type="resident"):
    """
    Trace Custom Registration
    """
    if request.site and request.site.site_status == 1:

        user = User.objects.get(pk=request.user.id) if (request.user.id) else None
        site = WyvernSite.objects.get(pk=request.site.id) or None

        # Prepare Context
        context = {"site": site}

        # Load Registration Forms
        context["resident_form"] = WyvernResidentForm(
            request.POST or None,
            instance=request.user if request.user.is_authenticated else None,
            initial={"site": request.site.id},
            auto_id="resident_%s",
        )

        context["establishment_form"] = WyvernEstablishmentForm(
            request.POST or None,
            instance=request.user if request.user.is_authenticated else None,
            initial={"site": request.site.id, "is_establishmen": True},
            auto_id="establishment_%s",
        )

        # Registration
        if request.method == "POST":
            next_url = (
                urllib.parse.unquote(request.GET.get("next"))
                if (request.GET.get("next"))
                else "/"
            )

            if type == "resident":
                form = context["resident_form"]

            if type == "establishment":
                form = context["establishment_form"]

            if form.is_valid():

                user = form.save(commit=False)

                if type == "establishment":
                    user.is_location = True

                # Cleaned(normalized) data
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                # Use set_password here
                user.set_password(password)
                user.save()

                user = authenticate(username=username, password=password)

                if user == None:
                    messages.add_message(request, 20, "Your account has been created")
                    return redirect("/accounts/login/")

                else:
                    messages.add_message(
                        request,
                        20,
                        "Welcome to {} {}!".format(
                            request.site.site_name, user.first_name
                        ),
                    )
                    login(request, user)
                    return redirect(reverse("trace-dashboard-user"))

        site_template = "themes/trace/pages/signup.html"
        return render(request, site_template, context)


@wyvern_core
def generated(request):

    context = {}

    return render(request, "themes/trace/pages/generated.html", context)


@wyvern_core
def map(request):

    if request.user.is_authenticated:

        locations = User.objects.filter(is_location=True).all()
        logs = WyvernTraceLog.objects.all()

        context = {"locations": locations, "logs": logs}

        if request.user.is_location:
            context["logs"] = WyvernTraceLog.objects.filter(
                wyvern_location=request.user
            ).order_by("-id")[:10]
        else:
            context["logs"] = WyvernTraceLog.objects.filter(
                wyvern_user=request.user
            ).order_by("-id")[:10]

        return render(request, "themes/trace/pages/map.html", context)

    else:

        return redirect("/")


@csrf_exempt
def fetch(request, uuid=""):
    if not request.GET:
        return JsonResponse({"Forbidden": "Method Not Allowed"})

    if not request.GET.get("auth_token") == "bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh":
        return JsonResponse({"Forbidden": "Unauthorized"})

    wyvern_user_data = User.objects.filter(uuid=uuid).get()

    if wyvern_user_data:
        return JsonResponse(
            {
                "Authentication": "True",
                "user": {
                    "uuid": wyvern_user_data.uuid,
                    "first_name": wyvern_user_data.first_name,
                    "last_name": wyvern_user_data.last_name,
                    "address": wyvern_user_data.address,
                    "phone": wyvern_user_data.phone,
                },
            }
        )

    else:
        return JsonResponse({"Authentication": "False"})


@csrf_exempt
def fetch_logs(request, user_id=""):
    if not request.GET:
        return JsonResponse({"Forbidden": "Method Not Allowed"})

    if not request.GET.get("auth_token") == "bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh":
        return JsonResponse({"Forbidden": "Unauthorized"})

    wyvern_user_data = User.objects.filter(pk=user_id).get()

    if wyvern_user_data:
        return JsonResponse(
            {
                "Authentication": "True",
                "user": serializers.serialize(
                    "json",
                    [
                        wyvern_user_data,
                    ],
                ),
            }
        )

    else:
        return JsonResponse({"Authentication": "False"})


@csrf_exempt
def log(request, uuid=""):
    if not request.POST:
        return JsonResponse({"Forbidden": "Method Not Allowed"})

    # if not request.POST.get('auth_token') == 'bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh':
    #     return JsonResponse({'Forbidden': 'Unauthorized'})

    wyvern_user_data = User.objects.get(uuid=uuid)

    if wyvern_user_data:
        """
        Create Location Log
        """
        wyvern_location_uuid = request.POST.get("location_uuid")

        if wyvern_location_uuid:
            wyvern_location_data = User.objects.get(uuid=wyvern_location_uuid)

            if wyvern_location_data.is_location:

                trace_log = WyvernTraceLog(
                    wyvern_user=wyvern_user_data,
                    wyvern_location=wyvern_location_data,
                    wyvern_temperature=request.POST.get("temperature"),
                )

            else:

                return JsonResponse(
                    {
                        "Authentication": "True",
                        "error": "Cannot log resident as location",
                    }
                )

            trace = trace_log.save()

            return JsonResponse({"Authentication": "True", "success": "Log saved"})

        else:

            return JsonResponse(
                {
                    "Authentication": "True",
                    "error": "Could not save log",
                }
            )

    else:
        return JsonResponse({"Authentication": "False"})


def manual_log(request):
    pass


""" End wyvernmetamorph/views.py """
