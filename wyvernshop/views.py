"""
Wyvern Shop - Views

"""
import wyvern.util.config as config

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render

from wyvern.util.sites import fetch_sites
from wyvern.util.chidori import wyvern_core

from wyvernsite.models import WyvernSite
from wyvernshop.models import WyvernProduct

from wyvernshop.forms import WyvernProductForm

from wyvernshop.product import *
from wyvernshop.product_category import *
from wyvernshop.cart import *
from wyvernshop.checkout import *
from wyvernshop.payment_methods import *
from wyvernshop.shipping_methods import *


@wyvern_core
def index(request, site=""):

    if request.wyvern:
        return render(
            request,
            "shop.html",
            {
                "page": "shop",
                "template_action": "shop/product/list.html",
                "sites": user_sites,
            },
        )

    else:
        site_template = "themes/{}/shop/catalog/pages/index.html".format(
            request.site.site_template
        )
        return render(request, site_template)
