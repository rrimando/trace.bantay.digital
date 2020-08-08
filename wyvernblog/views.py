"""
Wyvern Blog - Views

"""
import wyvern.util.config as config

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from wyvern.util.sites import fetch_sites
from wyvern.util.chidori import wyvern_core

from wyvernsite.models import WyvernSite
from wyvernblog.models import WyvernPost

from wyvernblog.forms import WyvernPostForm


@wyvern_core
def index(request, site=""):
    if request.wyvern:
        return render(
            request,
            "blog.html",
            {"page": "blog", "template_action": "blog/list.html", "sites": user_sites,},
        )
    else:
        site_template = "themes/{}/blog/pages/index.html".format(
            request.site.site_template
        )
        return render(request, site_template)


@wyvern_core
def create(request, site=""):
    if request.method == "POST":
        form = WyvernPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Process form data
            form.save()
            return redirect(reverse("site-manage", kwargs={"site": site}))
    else:
        form = WyvernPostForm(
            initial={
                "post_site": request.site,
                "post_author": request.user,
                "post_type": request.GET.get("post_type", "post"),
            }
        )

    return render(
        request, "blog.html", {"template_action": "blog/create.html", "form": form}
    )


@wyvern_core
def list(request):
    if request.wyvern:
        return render(
            request,
            "blog.html",
            {"page": "blog-list", "template_action": "blog/list.html"},
        )
    else:
        # TODO: Point to front end blog list page
        site_template = "themes/{}/blog/pages/list.html".format(
            request.site.site_template
        )
        return render(request, site_template)


@wyvern_core
def view(request, slug=""):
    post = get_object_or_404(
        WyvernPost.objects.filter(post_slug=slug, post_site=request.site)
    )
    site = WyvernSite.objects.get(site_url=request.site.site_url)
    site_template = "themes/{}/blog/pages/single.html".format(site.site_template)
    return render(request, site_template, {"page": "post", "post": post})


@wyvern_core
def edit(request, slug="", site=""):
    # TODO: Slug has to be unique --- Fix either add site url to params or modify slug
    """
        Bug the correct way to fetch this is with the site url/id -- but doing so will return a blank
    """
    post_site = WyvernSite.objects.get(site_url=site)
    post = WyvernPost.objects.filter(post_slug=slug, post_site=post_site).first()
    if request.method == "POST":
        form = WyvernPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # Process form data
            form.save()
            return redirect(reverse("site-manage", kwargs={"site": post_site.site_url}))
    else:
        form = WyvernPostForm(instance=post)

    return render(
        request,
        "blog.html",
        {"template_action": "blog/edit.html", "form": form, "post_site": post_site},
    )


@wyvern_core
def delete(request, slug="", site=""):
    # Load manager based on site type

    post_site = WyvernSite.objects.get(site_url=site)
    post = WyvernPost.objects.filter(post_slug=slug, post_site=post_site).first()

    if post:
        post.delete()

    return redirect(reverse("site-manage", kwargs={"site": site}))


# Built In Custom Post Types

# Custom Job Type - Note that this is a sub post type
@wyvern_core
def jobs(request):
    if request.wyvern:
        return render(
            request, "blog.html", {"page": "Jobs", "template_action": "blog/list.html"}
        )
    else:
        # TODO: Point to front end blog list page
        site_template = "themes/{}/blog/pages/jobs.html".format(
            request.site.site_template
        )
        return render(request, site_template, {"page": "Jobs"})


""" End wyvernblog/views.py """
