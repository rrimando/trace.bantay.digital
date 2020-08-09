from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group

from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite


# class WyvernLocation(models.Model):
#     pass

# class WyvernTraceUserInfo(models.Model):
#     pass


class WyvernTraceLog(models.Model):

    wyvern_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="public_user",
    )
    wyvern_location = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="location_user",
    )
    wyvern_temperature = models.CharField(max_length=255, null=True, blank=True)
    wyvern_trace_date = models.DateTimeField(auto_now_add=True, blank=True)

    @classmethod
    def create(cls, wyvern_user):
        trace = cls(wyvern_user=wyvern_user)
        return trace


class WyvernMedicalForm(models.Model):
    pass