"""
WYVERN DATA STORE - MODELS

Stores JSON data for retrieval of applications

"""
from django.db import models
from django.contrib.auth.models import User

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernDataStore(models.Model):

    data_store_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, blank=True, null=True
    )
    data_store_identity = models.CharField(max_length=255, blank=True, null=True)
    data_store_content = models.TextField(blank=True, null=True)
    data_store_tags = models.TextField(blank=True, null=True)
    data_store_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    data_store_status = models.IntegerField(default=1, choices=choices(Status))


# TODO: Data Store for Images and other data types
