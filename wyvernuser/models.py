import uuid

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group

from wyvern.util.upload import get_file_path


class User(AbstractUser):
    genders = [("M", "male"), ("F", "female"), ("O", "Other")]

    # member_group = Group.objects.filter(name='member').first() or None
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits are allowed.",
    )

    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    dateofbirth = models.DateTimeField(auto_now_add=True)
    hometown = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    geolocation = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=genders, null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    # Wyvern 2.0
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True
    )  # validators should be a list
    site_id = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_location = models.BooleanField(default=False)
    accepted_terms = models.BooleanField(default=True)
    uuid = models.CharField(
        max_length=100, unique=True, blank=True, null=True, default=uuid.uuid4
    )

    REQUIRED_FIELDS = ["groups_id", "email"]

    # LGU Fields
    # Not the best way to filter users that fall under but for now
    resident_establishment_filter = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
