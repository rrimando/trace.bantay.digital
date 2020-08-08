"""

WYVERN THEME CORE - MODELS

Schema Design: 

https://docs.google.com/spreadsheets/d/1eps2dIHlUoAq2QI-ysHw6uhrH0vUHK_BX_yKDe6o8W0/edit#gid=0

Reference:

https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

"""
import wyvern.util.config as config

from django.db import models

# from django.contrib.auth.models import User

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernTheme(models.Model):

    wyverntheme_name = models.CharField(max_length=255, unique=True)
    wyverntheme_slug = models.CharField(max_length=255, unique=True)


class WyvernThemeConfig(models.Model):

    wyverntheme_site = models.OneToOneField(
        WyvernSite,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wyvernsite_theme_site",
    )
    wyverntheme_theme = models.OneToOneField(
        WyvernTheme,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wyvernsite_theme_theme",
    )
    wyverntheme_index_template = models.CharField(max_length=255, null=True, blank=True)
    wyverntheme_base_layout = models.CharField(max_length=255, null=True, blank=True)
    wyverntheme_header_template = models.CharField(
        max_length=255, null=True, blank=True
    )
    wyverntheme_footer_template = models.CharField(
        max_length=255, null=True, blank=True
    )
    wyverntheme_custom_css = models.TextField(null=True, blank=True)
    wyverntheme_custom_js = models.TextField(null=True, blank=True)
    wyverntheme_google_fonts = models.TextField(null=True, blank=True)
    wyverntheme_back_to_top = models.BooleanField(default=False)
    wyverntheme_gdpr = models.BooleanField(default=False)

    def custom_css(self):
        return [x.strip() for x in self.wyverntheme_custom_css.split("\n")]

    def custom_js(self):
        return [x.strip() for x in self.wyverntheme_custom_js.split("\n")]
