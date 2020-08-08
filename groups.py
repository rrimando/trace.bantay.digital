import os
import django
import rest_framework

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wyvern.settings")

django.setup()
from django.contrib.auth.models import Group


GROUPS = ["admin", "moderator", "editor", "member", "anonymous"]
MODELS = ["user"]

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
    if created:
        print("Created group {}".format(new_group))
