"""
WYVERN FORMS - MODELS
"""
import wyvern.util.config as config

from django.db import models

# from django.contrib.auth.models import User

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernForm(models.Model):

    wyvern_form_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    wyvern_form_title = models.CharField(max_length=255, null=True, blank=True)
    wyvern_form_description = models.TextField(null=True, blank=True)
    wyvern_form_subtitle = models.CharField(max_length=255, null=True, blank=True)
    wyvern_form_slug = models.CharField(max_length=255, null=True, blank=True)
    wyvern_form_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )  # TODO - Pull from config
    wyvern_form_status = models.IntegerField(choices=choices(Status))
    wyvern_form_configuration = models.TextField(null=True, blank=True)
    wyvern_form_related_model = models.CharField(max_length=255, null=True, blank=True)
    wyvern_form_related_primary_key = models.CharField(
        max_length=255, null=True, blank=True
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Form: {} ({})".format(
            self.wyvern_form_title, self.wyvern_form_site.site_url
        )


"""Wyvern Forms Models EOF"""
