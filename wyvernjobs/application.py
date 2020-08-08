from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core
from wyvern.util.upload import get_file_path, handle_uploaded_file

from django import template
from django.contrib import messages

from wyvernsite.models import WyvernSite
from wyvernuser.models import User

from wyvernjobs.models import WyvernJobs, WyvernJobApplicant, WyvernJobApplication
from wyvernjobs.forms import (
    WyvernJobForm,
    WyvernJobApplicantForm,
    WyvernJobApplicationForm,
)


@wyvern_core
def application_index(request):

    return HttpResponse("applicant-list")


@wyvern_core
def application_create(request, site=""):

    current_site = WyvernSite.objects.filter(site_url=site).first()
    user = User.objects.get(pk=request.user.id) if request.user.id else None
    job = WyvernJobs.objects.get(pk=request.POST.get("job_application_job"))

    # Fetch The Applicant
    try:
        # applicant = WyvernJobApplicant.objects.get(job_applicant_user=user)
        applicant = WyvernJobApplicant.objects.get(
            job_applicant_email=request.POST.get("job_application_email")
        )
    except WyvernJobApplicant.DoesNotExist:
        applicant = None

    application_form = WyvernJobApplicationForm(request.POST, request.FILES)
    applicant_form = WyvernJobApplicantForm(
        request.POST, request.FILES, instance=applicant
    )

    # Check Application
    try:
        application = WyvernJobApplication.objects.get(
            job_application_applicant=applicant, job_application_job=job
        )

    except WyvernJobApplication.DoesNotExist:
        application = None

    if application:
        messages.add_message(
            request,
            messages.INFO,
            "You already have a pending application to this job.",
        )
        return redirect("/")

    if request.method == "POST":

        if application_form.is_valid() and applicant_form.is_valid():

            if applicant:
                # If applicant is a Wyvern User
                applicant.job_applicant_firstname = request.POST.get(
                    "job_applicant_firstname"
                )
                applicant.job_applicant_lastname = request.POST.get(
                    "job_applicant_lastname"
                )
                applicant.job_applicant_title = request.POST.get("job_applicant_title")
                applicant.job_applicant_email = request.POST.get("job_applicant_email")
                applicant.job_applicant_number = request.POST.get(
                    "job_applicant_number"
                )
                applicant.job_applicant_introduction = request.POST.get(
                    "job_applicant_introduction"
                )
                # TODO: Bug
                # applicant.job_applicant_resume     = request.FILES['job_applicant_resume']

                applicant.save()
            else:
                # Create a new applicant
                applicant = applicant_form.save()

            new_application = application_form.save(commit=False)
            new_application.job_application_applicant_id = applicant.id
            new_application.save()
            application_form.save_m2m()

            if request.POST["next"]:
                message = "Please continue and fill up the compliance form below."
            else:
                message = "Your application has been sent, we will be in touch."

            messages.add_message(request, messages.INFO, message)

        else:

            # for error in application_form.errors:
            #     messages.add_message(request, messages.ERROR, error)

            # for error in applicant_form.errors:
            #     messages.add_message(request, messages.ERROR, error)

            messages.add_message(
                request, messages.INFO, "There was a problem with your application."
            )

        return HttpResponseRedirect(
            request.POST["next"] or request.META.get("HTTP_REFERER", "/")
        )
    else:
        return HttpResponse("application-create")


@wyvern_core
def application_view(request, id=""):

    return HttpResponse("application-view")


@wyvern_core
def application_edit(request, slug=""):

    return HttpResponse("application-edit")


@wyvern_core
def application_delete(request, slug=""):

    return HttpResponse("application-delete")
