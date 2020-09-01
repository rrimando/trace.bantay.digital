"""
    Wyvern Core Decorator

    Determines if a site is being viewed from the backend or is being served on the front
"""
import wyvern.util.config as config

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from wyvern.util.sites import fetch_sites
from wyvernsite.models import WyvernSite


def wyvern_core(func):
    def wrap(request, *args, **kwargs):
        """ Current site being view or managed """
        try:
            kwargs["site"]
        except KeyError:
            # try:
            request.site_url = request.META["HTTP_HOST"]
            # except AttributeError:
            #     request.site_url = None
        else:
            request.site_url = kwargs["site"]

        request.site_url = (request.site_url).replace("www.", "")

        """ Server/POD available sites """
        available_sites = config.get("hosts", "allowed").split("\n")

        # Site URL
        if request.site_url in available_sites:
            """TODO: check if logged in"""

            """If we're managing through the wyvern dashboard"""
            if request.site_url == config.get("application", "server_url"):
                """
                Oh you may be managing from the dashboard, let's check if you own it
                TODO: Add check if you have permissions
                """
                request.wyvern = True
                if request.user.is_authenticated:
                    request.site = (
                        WyvernSite.objects.filter(
                            site_url=request.site_url, site_owner_id=request.user.id
                        ).first()
                        or None
                    )

                else:
                    request.site = None

            else:
                """or maybe a regular user"""
                request.wyvern = False
                request.site = (
                    WyvernSite.objects.filter(site_url=request.site_url).first() or None
                )

            """Here are all your available sites as well"""
            request.sites = fetch_sites(request) or None

            """Ok here you go"""
            return func(request, *args, **kwargs)

        else:
            raise PermissionDenied

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__

    return wrap
