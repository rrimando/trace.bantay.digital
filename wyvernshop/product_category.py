"""
Wyvern Shop - Views - Product Categories

"""
from django.urls import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from wyvern.util.chidori import wyvern_core

from wyvernshop.models import (
    WyvernProduct,
    WyvernProductCategory,
    WyvernProductCategories,
)
from wyvernsite.models import WyvernSite

from wyvernshop.forms import WyvernProductForm, WyvernProductCategoryForm


@wyvern_core
def product_category_create(request, site=""):

    current_site = WyvernSite.objects.filter(site_url=site).first()

    if request.method == "POST":
        form = WyvernProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("site-manage", kwargs={"site": site}))
    else:
        form = WyvernProductCategoryForm(
            initial={"product_category_site": current_site}
        )

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/product_category/create.html",
            "sites": request.sites,
            "form": form,
        },
    )


@wyvern_core
def product_category_list(request):

    return HttpResponse("Product Category List")


@wyvern_core
def product_category_view(request, slug=""):

    product_category = get_object_or_404(
        WyvernProductCategory.objects.filter(product_category_slug=slug)
    )
    products = WyvernProductCategories.objects.filter(
        product_categories_category=product_category
    ).all()
    site = WyvernSite.objects.filter(
        pk=product_category.product_category_site.id
    ).first()
    site_template = "themes/{}/shop/product_category/pages/single.html".format(
        site.site_template
    )
    return render(
        request,
        site_template,
        {
            "site": site,
            "page": "product-category",
            "product_category": product_category,
            "products": products,
        },
    )

    return HttpResponse("Product Category View")


@wyvern_core
def product_category_edit(request, slug=""):

    product_category = get_object_or_404(
        WyvernProductCategory.objects.filter(product_category_slug=slug)
    )

    if request.method == "POST":
        form = WyvernProductCategoryForm(
            request.POST, request.FILES, instance=product_category
        )
        if form.is_valid():
            # Process form data
            form.save()
            return redirect(
                reverse(
                    "site-manage",
                    kwargs={"site": product_category.product_category_site.site_url},
                )
            )
    else:
        form = WyvernProductCategoryForm(instance=product_category)

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/product_category/edit.html",
            "form": form,
            "sites": request.sites,
        },
    )


@wyvern_core
def product_category_delete(request, slug=""):

    # Load manager based on site type
    product_category = WyvernProductCategory.objects.filter(
        product_category_slug=slug
    ).first()
    site = product_category.product_category_site.site_url

    product_category.delete()
    return redirect(reverse("site-manage", kwargs={"site": site}))


"""EOF"""
