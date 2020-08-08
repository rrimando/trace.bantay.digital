"""
Wyvern LMS - Views

"""
import wyvern.util.config as config

from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render, get_object_or_404

from wyvern.util.sites import fetch_sites
from wyvern.util.chidori import wyvern_core

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernlms.models import WyvernLMSStudent

from wyvernlms.forms import WyvernLMSStudentForm
from wyvernuser.forms import WyvernUserForm


@wyvern_core
def index(request, site=""):

    if request.wyvern:

        return render(
            request,
            "lms.html",
            {
                "page": "lms",
                "template_action": "lms/list.html",
                # 'sites': request.user.sites,
            },
        )

    else:

        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
        else:
            user = None

        enrollment_data = (
            WyvernLMSStudent.objects.filter(wyvernlms_wyvern_user=user).first()
            if request.user.is_authenticated
            else None
        )

        if request.method == "POST":
            form = WyvernLMSStudentForm(request.POST, request.FILES)
            user_form = WyvernUserForm(request.POST, request.FILES)
            # Create User and then Enroll User
            next_url = (
                urllib.parse.unquote(request.GET.get("next"))
                if (request.GET.get("next"))
                else "/"
            )

            if form.is_valid() and user_form.is_valid():

                user = user_form.save(commit=False)

                # Cleaned(normalized) data
                username = user_form.cleaned_data["username"]
                password = user_form.cleaned_data["password"]

                # Use set_password here
                user.set_password(password)
                user.save()

                # Process enrollment form data
                enrollment = form.save(commit=False)
                enrollment.wyvernlms_wyvern_user = user
                enrollment.wyvernlms_wyvern_site = request.site
                enrollment.save()

                user = authenticate(username=username, password=password)

                if user == None:
                    messages.add_message(
                        request, 20, "Your account could not be been created"
                    )
                    return redirect("/login/")

                else:
                    login(request, user)
                    return redirect(next_url)
        else:
            user_form = WyvernUserForm(
                initial={"wyvernuser_site": request.site}, instance=enrollment_data
            )
            form = WyvernLMSStudentForm(
                initial={"wyvernlms_wyvern_site": request.site}, instance=user
            )

        site_template = "themes/{}/lms/action/enroll.html".format(
            request.site.site_template
        )

        context = {"form": form, "user_form": user_form}

        # This should be decouple or removed so that this module will be independent of custom code
        for key in request.GET:
            context[key.replace("-", "_")] = request.GET.get(key)

        return render(request, site_template, context)


@wyvern_core
def enroll(request):

    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
    else:
        user = None

    enrollment_data = (
        WyvernLMSStudent.objects.filter(wyvernlms_wyvern_user=user).first()
        if request.user.is_authenticated
        else None
    )

    if request.method == "POST":
        form = WyvernLMSStudentForm(request.POST, request.FILES)
        user_form = WyvernUserForm(request.POST, request.FILES)
        # Create User and then Enroll User
        next_url = (
            urllib.parse.unquote(request.GET.get("next"))
            if (request.GET.get("next"))
            else "/"
        )

        if form.is_valid() and user_form.is_valid():

            user = user_form.save(commit=False)

            # Cleaned(normalized) data
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            # Use set_password here
            user.set_password(password)
            user.save()

            # Process enrollment form data
            enrollment = form.save(commit=False)
            enrollment.wyvernlms_wyvern_user = user
            enrollment.wyvernlms_wyvern_site = request.site
            enrollment.save()

            user = authenticate(username=username, password=password)

            if user == None:
                messages.add_message(
                    request, 20, "Your account could not be been created"
                )
                return redirect("/login/")

            else:
                login(request, user)
                return redirect(next_url)
    else:
        user_form = WyvernUserForm(
            initial={"wyvernuser_site": request.site}, instance=enrollment_data
        )
        form = WyvernLMSStudentForm(
            initial={"wyvernlms_wyvern_site": request.site}, instance=user
        )

    context = {
        "template_action": "lms/enroll.html",
        "form": form,
        "user_form": user_form,
    }

    # This should be decouple or removed so that this module will be independent of custom code
    for key in request.GET:
        context[key.replace("-", "_")] = request.GET.get(key)

    return render(request, "lms.html", context)


""" End wyvernlms/views.py """
