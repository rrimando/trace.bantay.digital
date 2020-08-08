"""

WYVERN BLOG - MODELS

Schema Design: 

https://docs.google.com/spreadsheets/d/1eps2dIHlUoAq2QI-ysHw6uhrH0vUHK_BX_yKDe6o8W0/edit#gid=0

Reference:

https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

"""
from django.db import models
from django.contrib.auth.models import User

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernPost(models.Model):

    # TODO: Move this to a configurable end
    wyvern_post_types = [
        ("post", "Post"),
        ("page", "Page"),
        ("job", "Job"),
        ("custom", "Custom")  # Configurable
        # Booking
    ]

    post_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255)
    post_slug = models.CharField(max_length=255, unique=True, blank=True, null=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post_type = models.CharField(
        max_length=100, choices=wyvern_post_types, default="post"
    )
    post_content = models.TextField(null=True, blank=True)
    post_thumbnail = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    # TODO: Create linked page maker and use CMS content types the string below just loads a template from the carousel partials
    post_custom_template = models.CharField(
        max_length=255, null=True, blank=True, default=""
    )
    post_carousel = models.CharField(max_length=255, null=True, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    # SEO Values
    post_seo_author = models.CharField(max_length=255, null=True, blank=True)
    post_keywords = models.CharField(max_length=255, null=True, blank=True)
    post_description = models.TextField(null=True, blank=True)

    def get_thumb_url(self):
        try:
            # or whatever causes the exception
            return self.post_thumbnail.url
        except ValueError:
            return None


# TODO: WyvernPostCategory
class WyvernPostCategory:
    pass


class WyvernCMSContent:
    pass
