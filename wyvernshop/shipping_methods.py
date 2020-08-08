"""
Wyvern Shop - Views - Shipping Methods

"""
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, resolve

from wyvern.util.chidori import wyvern_core

from wyvernshop.models import WyvernProduct, WyvernShippingMethod
from wyvernsite.models import WyvernSite

from wyvernshop.forms import WyvernShippingMethodForm


@wyvern_core
def shipping_method_create(request, site=""):

    current_site = WyvernSite.objects.filter(site_url=site).first()

    if request.method == "POST":
        form = WyvernShippingMethodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("site-manage", kwargs={"site": site}))
    else:
        form = WyvernShippingMethodForm(initial={"shipping_method_site": current_site})

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/shipping_methods/create.html",
            "sites": request.sites,
            "form": form,
        },
    )


@wyvern_core
def shipping_method_list(request):

    return HttpResponse("List products")


@wyvern_core
def shipping_method_view(request, id=""):

    shipping_method = get_object_or_404(WyvernShippingMethod.objects.filter(pk=id))
    site = WyvernSite.objects.filter(pk=product.shipping_method_site.id).first()

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/shipping_methods/view.html",
            "page": "shipping-method",
            "sites": request.sites,
            "shipping_method": shipping_method,
        },
    )


@wyvern_core
def shipping_method_edit(request, id=""):

    shipping_method = WyvernShippingMethod.objects.filter(pk=id).first()

    if request.method == "POST":
        form = WyvernShippingMethodForm(
            request.POST, request.FILES, instance=shipping_method
        )
        if form.is_valid():
            # Process form data
            form.save()
            return redirect(
                reverse(
                    "site-manage",
                    kwargs={"site": shipping_method.shipping_method_site.site_url},
                )
            )
    else:
        form = WyvernShippingMethodForm(instance=shipping_method)

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/shipping_methods/edit.html",
            "shipping_method": shipping_method,
            "form": form,
            "sites": request.sites,
        },
    )


@wyvern_core
def shipping_method_delete(request, id=""):

    # Load manager based on site type
    shipping_method = WyvernShippingMethod.objects.filter(pk=id).first()
    site = shipping_method.shipping_method_site.site_url

    shipping_method.delete()
    return redirect(reverse("site-manage", kwargs={"site": site}))


"""EOF"""
