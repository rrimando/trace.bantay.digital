"""
Wyvern Shop - Views - Payment Methods

"""
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, resolve

from wyvern.util.chidori import wyvern_core

from wyvernshop.models import WyvernProduct, WyvernPaymentMethod
from wyvernsite.models import WyvernSite

from wyvernshop.forms import WyvernPaymentMethodForm


@wyvern_core
def payment_method_create(request, site=""):

    current_site = WyvernSite.objects.filter(site_url=site).first()

    if request.method == "POST":
        form = WyvernPaymentMethodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("site-manage", kwargs={"site": site}))
    else:
        form = WyvernPaymentMethodForm(initial={"payment_method_site": current_site})

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/payment_methods/create.html",
            "sites": request.sites,
            "form": form,
        },
    )


@wyvern_core
def payment_method_list(request):

    return HttpResponse("List products")


@wyvern_core
def payment_method_view(request, id=""):

    payment_method = get_object_or_404(WyvernPaymentMethod.objects.filter(pk=id))
    site = WyvernSite.objects.filter(pk=product.payment_method_site.id).first()

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/payment_methods/view.html",
            "page": "shipping-method",
            "sites": request.sites,
            "payment_method": payment_method,
        },
    )


@wyvern_core
def payment_method_edit(request, id=""):

    payment_method = WyvernPaymentMethod.objects.filter(pk=id).first()

    if request.method == "POST":
        form = WyvernPaymentMethodForm(
            request.POST, request.FILES, instance=payment_method
        )
        if form.is_valid():
            # Process form data
            form.save()
            return redirect(
                reverse(
                    "site-manage",
                    kwargs={"site": payment_method.payment_method_site.site_url},
                )
            )
    else:
        form = WyvernPaymentMethodForm(instance=payment_method)

    return render(
        request,
        "shop.html",
        {
            "template_action": "shop/payment_methods/edit.html",
            "payment_method": payment_method,
            "form": form,
            "sites": request.sites,
        },
    )


@wyvern_core
def payment_method_delete(request, id=""):

    # Load manager based on site type
    payment_method = WyvernPaymentMethod.objects.filter(pk=id).first()
    site = payment_method.payment_method_site.site_url

    payment_method.delete()
    return redirect(reverse("site-manage", kwargs={"site": site}))
