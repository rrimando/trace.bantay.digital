"""
    Site Context 
"""
import wyvern.util.config as config

from wyvernsite.models import WyvernSite


def core(request, *args, **kwargs):
    print("running context processors", request.site_url, args, kwargs)


def spam_filters(request):
    return {"spam_filters": config.get("filter", "filters").split("\n")}
