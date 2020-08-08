from django.urls import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core

from django import template

from wyvernsite.models import WyvernSite
from wyvernjobs.models import WyvernJobs

from wyvernjobs.forms import WyvernJobForm


@wyvern_core
def jobs_board(request, site=""):

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
