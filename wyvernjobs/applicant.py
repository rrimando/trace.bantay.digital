from django.urls import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core

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
def applicant_list(request, pk=""):

    job = WyvernJobs.objects.get(pk=pk)
    applicantions = WyvernJobApplication.objects.filter(job_application_job=job).all()
    applicant_info = []

    for applicant in applicantions:
        applicant_info.append(
            {
                "applicant": applicant,
                "wyvernuser": User.objects.get(
                    pk=applicant.job_application_applicant_user.id
                )
                if applicant.job_application_applicant_user
                else None,
            }
        )

    return render(
        request,
        "jobs.html",
        {
            "template_action": "jobs/applicant/list.html",
            "job": job,
            "applicants": applicant_info,
            "sites": request.sites,
        },
    )
