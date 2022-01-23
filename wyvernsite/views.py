"""
Wyvern Site - Views

"""
import wyvern.util.config as config

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render

from wyvern.util.chidori import wyvern_core
from wyvern.util.sites import fetch_sites

from wyvernblog.models import WyvernPost
from wyvernshop.models import WyvernProduct

from .models import WyvernSite
from .forms import WyvernSiteForm


@wyvern_core
def index(request, site=""):

    if request.user.is_authenticated:

        return render(request, "site.html", {"template_action": "site/list.html"})

    else:

        return redirect("/")


@wyvern_core
def create(request):
    if request.method == "POST":
        form = WyvernSiteForm(request.POST, request.FILES)
        if form.is_valid():
            # Process form data
            form.save()
            return redirect(reverse("site-index"))
    else:
        form = WyvernSiteForm()

    return render(
        request, "site.html", {"template_action": "site/create.html", "form": form}
    )


@wyvern_core
def configure(request, site=""):

    if request.method == "POST":
        form = WyvernSiteForm(request.POST, request.FILES, instance=request.site)
        if form.is_valid():
            """Process form data"""
            form.save()
            """
                TODO: https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
                Flash message
            """
            return redirect(
                reverse("site-configure", kwargs={"site": request.site.site_url})
            )
    else:
        form = WyvernSiteForm(instance=request.site)

    return render(
        request, "site.html", {"template_action": "site/configure.html", "form": form}
    )


@wyvern_core
def manage(request, site=""):

    sections = config.get(site, "sections") or []

    """Load manager based on site type"""
    return render(
        request,
        "site.html",
        context={"template_action": "site/manage.html", "sections": sections},
    )


@wyvern_core
def delete(request, site=""):

    site = WyvernSite.objects.filter(site_url=site).first()
    sites = fetch_sites(request)

    if site in sites:
        site.delete()

    return redirect(reverse("site-index"))


""" End wyvernsite/views.py """
