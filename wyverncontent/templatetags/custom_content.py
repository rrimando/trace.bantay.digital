from django import template
from django.shortcuts import render
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.core.exceptions import ObjectDoesNotExist

from wyvernsite.models import WyvernSite
from wyverncontent.models import WyvernCustomContent

register = template.Library()


@register.filter(name="custom_content")
def custom_content(slug, site):

    try:
        site = WyvernSite.objects.filter(site_url=site).get()
        content, created = WyvernCustomContent.objects.get_or_create(
            wyvern_custom_content_slug=slug, wyvern_custom_content_site=site
        )

    except (AttributeError, ObjectDoesNotExist):

        content = None

    context = {
        "label": content.wyvern_custom_content_label,
        "slug": content.wyvern_custom_content_slug,
        "content": content.wyvern_custom_content_content,
    }

    template = "/var/www/wyvern/wyverncontent/templates/widget/content-view.html"
    rendered_content = render_to_string(template, context)
    return mark_safe(rendered_content)


@register.filter(name="custom_content_editor")
def custom_content_editor(label, site):

    try:
        site = WyvernSite.objects.filter(site_url=site).get()
        content, created = WyvernCustomContent.objects.get_or_create(
            wyvern_custom_content_slug=label, wyvern_custom_content_site=site
        )

    except (AttributeError, ObjectDoesNotExist):

        content = None

    context = {
        "label": content.wyvern_custom_content_label,
        "slug": content.wyvern_custom_content_slug,
        "content": content.wyvern_custom_content_content,
    }

    template = "/var/www/wyvern/wyverncontent/templates/widget/content-editor.html"
    rendered_content = render_to_string(template, context)
    return mark_safe(rendered_content)
