"""
    Wyvern Site Context 
"""
import wyvern.util.config as config

from .models import WyvernSite


def sites(request):

    try:
        request.site
    except AttributeError:
        site = None
    else:
        site = request.site
    try:
        request.sites
    except AttributeError:
        sites = None
    else:
        sites = request.sites

    return {"site": site, "sites": sites}
