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

from .models import WyvernSite, WyvernThemeConfig
from .forms import WyvernThemeConfigForm


@wyvern_core
def index(request, site=""):

    if request.user.is_authenticated:

        theme_config, created = WyvernThemeConfig.objects.get_or_create(
            wyverntheme_site=request.site
        )

        if request.method == "POST":

            form = WyvernThemeConfigForm(
                request.POST, request.FILES, instance=theme_config
            )
            if form.is_valid():
                # Process form data
                form.save()
                return redirect(reverse("site-manage", kwargs={"site": site}))

        else:
            form = WyvernThemeConfigForm(
                instance=theme_config, initial={"wyverntheme_site": request.site,}
            )

        return render(
            request,
            "theme.html",
            {"form": form, "template_action": "wyvern/theme/config.html"},
        )

    else:

        return redirect("/")


""" End wyvernthemes/views.py """
