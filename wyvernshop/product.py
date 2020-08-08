"""
Wyvern Shop - Views - Products

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

from wyvernshop.forms import WyvernProductForm, WyvernProductCategoriesForm


@wyvern_core
def product_create(request, site=""):

    current_site = WyvernSite.objects.filter(site_url=site).first()

    if request.method == "POST":
        form = WyvernProductForm(request.POST, request.FILES)
        product_category_form = WyvernProductCategoriesForm(request.POST, request.FILES)

        if form.is_valid():
            new_product = form.save()

            product = WyvernProduct.objects.filter(pk=new_product.pk).first()
            product_category_form = WyvernProductCategoriesForm(
                request.POST,
                request.FILES,
                initial={"product_categories_product": product},
            )

            if product_category_form.is_valid():
                product_category_form.save()

            return redirect(reverse("site-manage", kwargs={"site": site}))

    else:
        form = WyvernProductForm(initial={"product_site": current_site})
        product_category_form = WyvernProductCategoriesForm()

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/products/create.html",
            "sites": request.sites,
            "form": form,
            "product_category_form": product_category_form,
        },
    )


@wyvern_core
def product_list(request):

    site = request.site
    site_template = "themes/{}/shop/catalog/pages/index.html".format(site.site_template)

    return render(request, site_template, {"site": site, "page": "product"})


@wyvern_core
def product_view(request, slug=""):

    site = request.site

    product = get_object_or_404(WyvernProduct.objects.filter(product_slug=slug))
    product_category = WyvernProductCategories.objects.filter(
        product_categories_product=product
    ).first()

    site_template = "themes/{}/shop/product/pages/single.html".format(
        site.site_template
    )
    return render(
        request,
        site_template,
        {
            "site": site,
            "page": "product",
            "product": product,
            "product_category": product_category,
        },
    )


@wyvern_core
def product_edit(request, slug=""):

    product = WyvernProduct.objects.filter(product_slug=slug).first()
    product_category = WyvernProductCategories.objects.filter(
        product_categories_product=product
    ).first()

    if request.method == "POST":
        form = WyvernProductForm(request.POST, request.FILES, instance=product)
        product_category_form = WyvernProductCategoriesForm(
            request.POST, request.FILES, instance=product_category
        )

        if form.is_valid():
            # Process form data
            form.save()

            if product_category_form.is_valid():
                # Process form data
                product_category_form.save()

            return redirect(
                reverse("site-manage", kwargs={"site": product.product_site.site_url})
            )

    else:
        form = WyvernProductForm(instance=product)
        product_category_form = (
            WyvernProductCategoriesForm(instance=product_category)
            if product_category
            else WyvernProductCategoriesForm(
                initial={"product_categories_product": product}
            )
        )

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/products/edit.html",
            "form": form,
            "product_category_form": product_category_form,
            "sites": request.sites,
        },
    )


@wyvern_core
def product_delete(request, slug=""):

    # Load manager based on site type
    product = WyvernProduct.objects.filter(product_slug=slug).first()
    site = product.product_site.site_url

    product.delete()
    return redirect(reverse("site-manage", kwargs={"site": site}))


"""EOF"""
