"""
Wyvern Jobs - Views - Employers

"""
from django.urls import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core

from django import template

from wyvernsite.models import WyvernSite
from wyvernjobs.models import WyvernJobs

from wyvernjobs.forms import WyvernJobForm

from wyvernjobs.jobs import *
from wyvernjobs.applicant import *
from wyvernjobs.application import *
from wyvernjobs.employers import *


@wyvern_core
def index(request):

    site = request.site
    site_template = "themes/{}/jobs/list/pages/index.html".format(site.site_template)

    try:

        return render(request, site_template, {"site": site, "page": "job"})

    except template.TemplateDoesNotExist:

        return redirect("/")


"""EOF"""
