"""

WYVERN SITE CORE - MODELS

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
from wyvernutilities.models import Status


class WyvernSite(models.Model):
    # TODO: Move this to a configurable end
    wyvern_site_types = [
        ("blog", "Blog"),
        ("shop", "Shop"),
        ("hybrid", "Hybrid")  # Configurable
        # Booking
    ]

    # TODO: Move this to a configurable end
    wyvern_site_templates = [
        ("basic", "Basic"),  # TODO: Remove all hardcoded references to Site Name etc
        ("parallax", "Parallax"),
        ("taxproblem", "Tax Problem"),
        ("jobs", "Jobs"),
        ("jobscalle", "Jobs Calle Uno"),
        ("medical", "Medical"),
        ("techapp", "Tech Company"),
        ("backlinersph", "Backliners PH")
        # Booking
    ]

    site_url = models.CharField(max_length=255, unique=True)
    site_name = models.CharField(max_length=255)
    site_analytics = models.CharField(max_length=255, null=True, blank=True)
    site_subtitle = models.CharField(max_length=255, null=True, blank=True)
    site_favicon = models.ImageField(
        upload_to=get_file_path, null=True, blank=True, default=None
    )  # TODO - Pull from config
    site_logo = models.ImageField(
        upload_to=get_file_path, null=True, blank=True, default=None
    )  # TODO - Pull from config
    site_logo_dark = models.ImageField(
        upload_to=get_file_path, null=True, blank=True, default=None
    )  # TODO - Pull from config
    site_meta_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True, default=None
    )  # TODO - Pull from config
    site_status = models.IntegerField(choices=choices(Status))
    site_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    site_type = models.CharField(
        max_length=10, choices=wyvern_site_types, default="blog"
    )  # Pull from config
    site_template = models.CharField(
        max_length=50, choices=wyvern_site_templates, default="aggro"
    )  # Pull from config
    site_notifications_recipients = models.CharField(
        max_length=255, null=True, blank=True
    )
    site_notifications_from = models.CharField(max_length=255, null=True, blank=True)
    site_description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    # Contact Form Details
    site_email = models.CharField(max_length=255, null=True, blank=True)
    site_number = models.CharField(max_length=255, null=True, blank=True)
    site_number_alt = models.CharField(max_length=255, null=True, blank=True)
    site_google_map = models.TextField(null=True, blank=True)
    site_address = models.TextField(null=True, blank=True)

    # Basic Availabe Configurations for Sites
    site_google_verification = models.CharField(max_length=255, null=True, blank=True)
    site_recaptcha = models.CharField(max_length=255, null=True, blank=True)
    site_fb_admins = models.CharField(max_length=255, null=True, blank=True)
    site_addthis = models.CharField(max_length=255, null=True, blank=True)

    # Redirection Settings
    site_redirect = models.CharField(max_length=255, null=True, blank=True)

    def get_favicon_url(self):
        try:
            # or whatever causes the exception

            if self.site_favicon:
                return self.site_favicon.url
            else:
                return None

        except ValueError:
            return None

    def __str__(self):
        return "Site: {} ({})".format(self.site_name, self.site_url)


class WyvernSiteConfigOption(models.Model):
    site_config_option_name = models.CharField(max_length=20)
    site_config_option_validation = models.TextField(null=True, blank=True)
    site_config_option_values = models.TextField(null=True, blank=True)
    site_config_option_default = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernSiteConfig(models.Model):
    config_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    config_name = models.ForeignKey(WyvernSiteConfigOption, on_delete=models.CASCADE)
    config_value = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernModule(models.Model):
    module_name = models.CharField(max_length=255)
    module_slug = models.CharField(max_length=50)
    module_description = models.TextField()
    module_status = models.IntegerField(choices=choices(Status))
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernModuleConfigOption(models.Model):
    module_config_option_name = models.CharField(max_length=20)
    module_config_option_validation = models.TextField(null=True, blank=True)
    module_config_option_values = models.TextField(null=True, blank=True)
    module_config_option_default = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernSiteModules(models.Model):
    site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    site_module = models.ForeignKey(WyvernModule, on_delete=models.CASCADE)
    site_module_status = models.IntegerField(choices=choices(Status))
    date_active = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernSiteModuleConfig(models.Model):
    site_module_config_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    site_module_config_module = models.ForeignKey(
        WyvernModule, on_delete=models.CASCADE
    )
    site_module_config_name = models.ForeignKey(
        WyvernModuleConfigOption, on_delete=models.CASCADE
    )
    site_module_config_value = models.TextField(null=True, blank=True)


"""EOF"""
