"""

Wyvern Core - Views
    
"""
import urllib
from django.urls import reverse
import wyvern.util.config as config

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render

from wyvern.util.chidori import wyvern_core

from wyvernsite.models import WyvernSite
from wyvernblog.models import WyvernPost
from wyvernshop.models import WyvernProduct


@wyvern_core
def index(request):

    keyword = request.GET.get("keyword") or ""

    if request.wyvern:
        if request.user.is_authenticated:
            return render(request, "dashboard.html", {"page": "home"})

        else:
            return render(request, "search.html", {"page": "search"})

    else:
        """
            Serve the custom sites
        """

        products = WyvernProduct.objects.filter(
            product_site=request.site, product_name__icontains=keyword
        ).all()
        posts = WyvernPost.objects.filter(
            post_site=request.site, post_title__icontains=keyword, post_type="post"
        ).all()
        jobs = WyvernPost.objects.filter(
            post_site=request.site, post_title__icontains=keyword, post_type="job"
        ).all()

        if request.site:
            site_template = "themes/{}/search.html".format(request.site.site_template)
            return render(
                request,
                site_template,
                {
                    "keyword": keyword,
                    "result_count": str(
                        products.count() + posts.count() + jobs.count()
                    ),
                    "products": products,
                    "posts": posts,
                    "jobs": jobs,
                },
            )

        else:
            return HttpResponse(
                "Come back in a while as something awesome will here soon!"
            )
