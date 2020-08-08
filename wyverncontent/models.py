"""

WYVERN CUSTOM CONTENT - MODELS

"""
import wyvern.util.config as config

from django.db import models

# from django.contrib.auth.models import User

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernCustomContent(models.Model):

    wyvern_custom_content_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    wyvern_custom_content_label = models.CharField(
        max_length=255, null=True, blank=True
    )
    wyvern_custom_content_slug = models.CharField(max_length=255, null=True, blank=True)
    wyvern_custom_content_content = models.TextField(null=True, blank=True)
    wyvern_custom_content_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )


"""Wyvern Custom Content EOF"""
