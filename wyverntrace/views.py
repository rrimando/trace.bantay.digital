"""
Wyvern LMS - Views

"""
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

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from wyvernuser.forms import WyvernUserForm
from wyverntrace.forms import WyvernEstablishmentForm, WyvernResidentForm


@wyvern_core
def index(request, site=""):
    return redirect("/")


@wyvern_core
def dashboard(request):

    user = User.objects.get(pk=request.user.id) if (request.user.id) else None
    site = WyvernSite.objects.get(pk=request.site.id) or None

    # Prepare Context
    context = {
        'user': user,
        'site': site,
        'type': 'establishment' if user.is_location else 'resident'
    }

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
        initial={"site": request.site.id},
        auto_id="establishment_%s",
    )

    if request.user.is_authenticated:
        if request.user.is_location:
            context["logs"] = WyvernTraceLog.objects.filter(
                wyvern_location=request.user
            ).order_by("-id")[:10]
        else:
            context["logs"] = WyvernTraceLog.objects.filter(
                wyvern_user=request.user
            ).order_by("-id")[:10]

    else:
        return redirect("/")
        
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
        context = {
            'site': site
        }

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
            initial={"site": request.site.id},
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

                # Cleaned(normalized) data
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                # Use set_password here
                user.set_password(password)
                user.save()

                user = authenticate(username=username, password=password)

                if user == None:
                    messages.add_message(
                        request, 20, "Your account has been created"
                    )
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
                    return redirect(next_url)            

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
def fetch(request, user_id=""):
    if not request.GET:
        return JsonResponse({"Forbidden": "Method Not Allowed"})

    if not request.GET.get("auth_token") == "bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh":
        return JsonResponse({"Forbidden": "Unauthorized"})

    wyvern_user_data = User.objects.filter(pk=user_id).get()

    if wyvern_user_data:
        return JsonResponse(
            {
                "Authentication": "True",
                "user": serializers.serialize("json", [wyvern_user_data,]),
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
                "user": serializers.serialize("json", [wyvern_user_data,]),
            }
        )

    else:
        return JsonResponse({"Authentication": "False"})


@csrf_exempt
def log(request, user_id=""):
    if not request.POST:
        return JsonResponse({"Forbidden": "Method Not Allowed"})

    # if not request.POST.get('auth_token') == 'bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh':
    #     return JsonResponse({'Forbidden': 'Unauthorized'})

    wyvern_user_data = User.objects.get(pk=user_id)

    if wyvern_user_data:
        """
            Create Location Log
        """
        wyvern_location_id = request.POST.get("location_id")

        if wyvern_location_id:
            wyvern_location_data = User.objects.get(pk=wyvern_location_id)

            trace_log = WyvernTraceLog(
                wyvern_user=wyvern_user_data,
                wyvern_location=wyvern_location_data,
                wyvern_temperature=request.POST.get("temperature"),
            )

            trace = trace_log.save()

            return JsonResponse({"Authentication": "True", "success": "Log saved"})

        else:

            return JsonResponse(
                {"Authentication": "True", "error": "Could not save log",}
            )

    else:
        return JsonResponse({"Authentication": "False"})

""" End wyvernmetamorph/views.py """
