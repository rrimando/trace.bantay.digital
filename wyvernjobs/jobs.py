from django.urls import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core

from django import template

from wyvernsite.models import WyvernSite
from wyvernblog.models import WyvernPost
from wyvernshop.models import WyvernProduct
from wyvernuser.models import User

from wyvernjobs.models import WyvernJobs, WyvernJobApplicant, WyvernJobApplication
from wyvernjobs.forms import (
    WyvernJobForm,
    WyvernJobApplicantForm,
    WyvernJobApplicationForm,
)


@wyvern_core
def job_create(request, site=""):

    current_site = WyvernSite.objects.filter(site_url=site).first()

    if request.method == "POST":
        form = WyvernJobForm(request.POST, request.FILES)

        if form.is_valid():
            new_job = form.save()

            job = WyvernJobs.objects.filter(pk=new_job.pk).first()

            return redirect(reverse("site-manage", kwargs={"site": site}))

    else:
        form = WyvernJobForm(initial={"job_site": current_site})

    return render(
        request,
        "jobs.html",
        {
            "template_action": "jobs/job/create.html",
            "sites": request.sites,
            "form": form,
        },
    )


@wyvern_core
def job_list(request):

    site = request.site
    site_template = "themes/{}/job/list/pages/index.html".format(site.site_template)

    return render(request, site_template, {"site": site, "page": "job-list"})


@wyvern_core
def job_view(request, slug=""):

    site = request.site
    job = get_object_or_404(WyvernJobs.objects.filter(job_slug=slug))

    # For Jobs Sites
    # Fetch Initial Data

    # Fetch the applicant
    user = User.objects.get(pk=request.user.id) if (request.user.id) else None
    site = WyvernSite.objects.get(pk=request.site.id) or None
    applicant = None

    # Check If An Applicant Exists
    if user:
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
        applicant_form = WyvernJobApplicantForm(initial={"job_applicant_site": site})

    application_form = WyvernJobApplicationForm(
        initial={
            "job_application_applicant_user": user,
            "job_application_applicant": applicant.id if applicant else None,
            "job_application_site": site,
            "job_application_job": job.id,
        }
    )

    context = {
        "applicant_form": applicant_form,
        "application_form": application_form,
        "site": site,
        "page": "jobs",
        "job": job,
    }

    site_template = "themes/{}/jobs/job/pages/single.html".format(site.site_template)
    return render(request, site_template, context)


@wyvern_core
def job_edit(request, slug=""):

    job = WyvernJobs.objects.filter(job_slug=slug).first()

    if request.method == "POST":
        form = WyvernJobForm(
            request.POST,
            request.FILES,
            instance=job,
            initial={"job_site": job.job_site},
        )

        if form.is_valid():
            # Process form data
            form.save()

            return redirect(
                reverse("site-manage", kwargs={"site": job.job_site.site_url})
            )

    else:
        form = WyvernJobForm(instance=job)

    return render(
        request,
        "jobs.html",
        {
            "template_action": "jobs/job/edit.html",
            "form": form,
            "sites": request.sites,
        },
    )


@wyvern_core
def job_delete(request, slug=""):

    # Load manager based on site type
    job = WyvernJobs.objects.filter(job_slug=slug).first()
    site = job.job_site.site_url

    job.delete()
    return redirect(reverse("site-manage", kwargs={"site": site}))
