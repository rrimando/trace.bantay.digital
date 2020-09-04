import datetime

from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group
import datetime

from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvern.util.array import choices



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
    wyvern_first_name = models.CharField(max_length=255, default="")
    wyvern_last_name = models.CharField(max_length=255, default="")
    wyvern_phone_number = models.CharField(max_length=13, default="")
    wyvern_resident_address = models.CharField(max_length=255, default="")
    wyvern_temperature = models.CharField(max_length=255, null=True, blank=True)
    wyvern_trace_date = models.DateTimeField(auto_now_add=True, blank=True)

    @classmethod
    def create(cls, wyvern_user):
        trace = cls(wyvern_user=wyvern_user)
        return trace

    def get_first_name(self):
        return self.wyvern_first_name if self.wyvern_first_name else self.wyvern_user.first_name

    def get_last_name(self):
        return self.wyvern_last_name if self.wyvern_last_name else self.wyvern_user.last_name

    def get_phone_number(self):
        return self.wyvern_phone_number if self.wyvern_phone_number else self.wyvern_user.phone

    def get_resident_address(self):
        return self.wyvern_resident_address if self.wyvern_resident_address else self.wyvern_user.address


class WyvernMedicalForm(models.Model):
    wyvern_answer = (
        (0, ("No")),
        (1, ("Yes")),
    )

    wyvern_medical_form_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="wyvern_user",
    )

    wyvern_medical_form_date = models.DateField(default=datetime.date.today)
    wyvern_have_sore_throat = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_have_body_pain = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_have_head_ache = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_have_fever = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_near_covid = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_contact_symptoms = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_travelled_outside_philippines = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
    wyvern_travelled_ncr = models.IntegerField(
        choices=wyvern_answer,
        default=0,
    )
