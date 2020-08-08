from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group

from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite


class WyvernSubscribers(models.Model):
    subscription_status = [(0, "inactive"), (1, "active"), (2, "suspended")]

    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    sub_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, null=True, blank=True
    )
    sub_firstname = models.CharField(max_length=255, null=True, blank=True)
    sub_lastname = models.CharField(max_length=255, null=True, blank=True)
    sub_fullname = models.CharField(max_length=255, null=True, blank=True)
    sub_email = models.CharField(max_length=255, null=True, blank=True)
    sub_status = models.IntegerField(choices=subscription_status)
    sub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subscriber.email


# Todo for multiple subscription sites
class WyvernSubscriptions:
    pass
