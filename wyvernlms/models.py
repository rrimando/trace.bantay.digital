from django.db import models

# Create your models here.
"""

WYVERN SHOP - MODELS

Schema Design: 

TODO: https://docs.google.com/spreadsheets/d/1eps2dIHlUoAq2QI-ysHw6uhrH0vUHK_BX_yKDe6o8W0/edit#gid=0

Reference:

https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

"""
import wyvern.util.config as config
import datetime

from django.db import models

# from django.contrib.auth.models import User

from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField

from wyvern.util.array import choices, list_choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernLMSStudent(models.Model):

    # TODO: Move this to a configurable end
    wyvernlms_gender_types = [
        ("m", "Male"),
        ("f", "Female"),
        ("u", "Undisclosed"),
    ]

    current_year = datetime.datetime.today().year
    wyvernlms_year_graduated_options = list(range(current_year, current_year - 12, -1))

    wyvernlms_wyvern_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, blank=True, null=True, default=1
    )
    wyvernlms_wyvern_user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )

    wyvernlms_firstname = models.CharField(max_length=255)
    wyvernlms_middlename = models.CharField(max_length=255)
    wyvernlms_lastname = models.CharField(max_length=255)
    wyvernlms_birthdate = models.DateTimeField(blank=True, null=True)

    # https://uxdesign.cc/designing-forms-for-gender-diversity-and-inclusion-d8194cf1f51
    wyvernlms_gender = models.CharField(
        max_length=255,
        choices=wyvernlms_gender_types,
        default="u",
        blank=True,
        null=True,
    )

    wyvernlms_email_address = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    wyvernlms_mobile_number = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
