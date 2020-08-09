"""

Wyvern Core - Views
    
"""
import urllib
from django.urls import reverse
import wyvern.util.config as config

from django.contrib import messages
from django.contrib.auth import login, authenticate

# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse
from django.shortcuts import render

from wyvern.util.chidori import wyvern_core

from wyvernuser.forms import WyvernUserForm

from wyvernsite.models import WyvernSite
from wyvernblog.models import WyvernPost
from wyvernshop.models import WyvernProduct
from wyvernuser.models import User
from wyverntrace.models import WyvernTraceLog


from wyvernjobs.models import WyvernJobs, WyvernJobApplicant, WyvernJobApplication
from wyvernjobs.forms import (
    WyvernJobForm,
    WyvernJobApplicantForm,
    WyvernJobApplicationForm,
)


@wyvern_core
def index(request):

    if request.wyvern:
        if request.user.is_authenticated:
            return render(request, "dashboard.html", {"page": "home"})

        else:
            return render(request, "home.html", {"page": "home"})

    else:
        """
            Serve the custom sites
        """
        if request.site and request.site.site_status == 1:
            # Fetch Initial Data

            # Fetch the applicant
            user = User.objects.get(pk=request.user.id) if (request.user.id) else None
            site = WyvernSite.objects.get(pk=request.site.id) or None
            sections = config.get(site.site_url, "sections") or []

            # Prepare Context
            context = {}

            # For Jobs Sites
            if "jobs_section" in sections:
                if user:
                    # Check If An Applicant Exists
                    applicant, created = (
                        WyvernJobApplicant.objects.get_or_create(
                            job_applicant_user=user, job_applicant_site=site
                        )
                        or None
                    )

                    if applicant:
                        applicant_form = WyvernJobApplicantForm(instance=applicant)
                    else:
                        applicant_form = WyvernJobApplicantForm(
                            initial={
                                "job_applicant_user": user,
                                "job_applicant_site": site,
                                "job_applicant_email": user.email,
                            }
                        )
                else:
                    applicant_form = WyvernJobApplicantForm()

                application_form = WyvernJobApplicationForm(
                    initial={
                        "job_application_applicant": user,
                        "job_application_site": site,
                    }
                )

                context["applicant_form"] = applicant_form
                context["application_form"] = application_form

            # Registration
            if request.method == "POST":
                form = WyvernUserForm(request.POST, initial={"site": request.site.id})
                next_url = (
                    urllib.parse.unquote(request.GET.get("next"))
                    if (request.GET.get("next"))
                    else "/"
                )

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

                context["form"] = form

            else:

                # Load Login and Register Forms
                context["form"] = WyvernUserForm(
                    instance=request.user if request.user.is_authenticated else None,
                    initial={"site": request.site.id},
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

            site_template = "themes/{}/index.html".format(request.site.site_template)
            return render(request, site_template, context)

        else:
            return HttpResponse(
                "Come back in a while as something awesome will here soon!"
            )


@wyvern_core
def signup(request):

    if request.user.is_authenticated:
        return redirect(reverse("core-index"))

    if request.method == "POST":
        form = WyvernUserForm(request.POST)
        next_url = (
            urllib.parse.unquote(request.GET.get("next"))
            if (request.GET.get("next"))
            else "/"
        )

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
                messages.add_message(request, 20, "Your account has been created")
                return redirect("/accounts/login/")

            else:
                login(request, user)
                return redirect(next_url)

    else:
        form = WyvernUserForm({"site": request.site.id})

    return render(request, "registration/signup.html", {"form": form})


@wyvern_core
def dashboard(request):
    if request.user.is_authenticated:
        template = "basic" if request.site is None else request.site.site_template
        site_template = "themes/{}/user/pages/dashboard.html".format(template)
        return render(
            request,
            site_template,
            {
                # context
            },
        )
    else:
        return redirect("/accounts/login/")


@wyvern_core
def account(request):
    return HttpResponse("Account page is on the way!")


@wyvern_core
def profile(request):
    return HttpResponse("Profile page is on the way!")


# Custom Errors
@wyvern_core
def handler404(request, *args, **argv):
    # TODO CATCH ERROR AND EMAIL TO DEVELOPERS
    # return HttpResponse('Ooooh we could not find that resourse for you. But we are on it')
    return render(request, "404.html")


@wyvern_core
def handler500(request, *args, **argv):
    # MAIL ERROR AND EMAIL TO DEVELOPERS
    # return HttpResponse('Ooooh we could not find that resourse for you. But we are on it')
    return render(request, "404.html")


# Common Page Routes
# Contact
# About Us
