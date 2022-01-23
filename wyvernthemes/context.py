"""
    Wyvern Themes Context 
"""
import wyvern.util.config as config

from .models import WyvernThemeConfig
from wyvern.util.chidori import wyvern_core

# This might not be the best way to display custom posts
def themes(request):
    wyvern_site_templates = [
        "basic",  # TODO: Remove all hardcoded references to Site Name etc
        "parallax",
        "taxproblem",
        "jobs",
        "jobscalle",
        "medical",
        "techapp",
        # Booking
    ]

    return {"themes": wyvern_site_templates}


@wyvern_core
def theme_config(request):

    try:
        request.site
    except AttributeError:
        theme_config = None
    else:
        # TODO: Make fetching theme dynamic

        theme_config, created = WyvernThemeConfig.objects.get_or_create(
            wyverntheme_site=request.site
        )

        if not theme_config.wyverntheme_base_layout:
            if request.wyvern:
                theme_config.wyverntheme_base_layout = "base.html"
            else:
                theme_config.wyverntheme_base_layout = (
                    "themes/basic/base/basic-base.html"
                )

    return {"theme_config": theme_config}
