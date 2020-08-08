"""
Wyvern Shop - Views - Cart

TODO: Refactor redundant code

"""
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, resolve

from wyvern.util.chidori import wyvern_core
from wyvern.util.url import custom_redirect

from wyvernsite.models import WyvernSite
from wyvernshop.models import WyvernProduct, WyvernCart, WyvernCartItem


@wyvern_core
def cart_add(request):

    current_url = request.get_full_path()

    # TODO Move is request authenticated to chidori
    if request.user.is_authenticated:
        # Detect if user has a pending/uncompleted cart
        cart, created = WyvernCart.objects.get_or_create(
            cart_customer=request.user, cart_status="current"
        )

        product_id = (
            request.POST.get("product_id")
            if request.POST.get("product_id")
            else request.GET.get("product_id")
        )  # TODO: Handle error
        product_quantity = (
            request.POST.get("product_quantity")
            if request.POST.get("product_quantity")
            else request.GET.get("product_quantity")
        )  # TODO: Handle error
        product = get_object_or_404(WyvernProduct.objects.filter(pk=product_id))

        if cart:
            cart_item, created = WyvernCartItem.objects.get_or_create(
                cart_cart=cart, cart_product_id=product_id
            )

            # Update the quantity
            cart_item.cart_product_quantity = (
                int(cart_item.cart_product_quantity) + int(product_quantity)
                if cart_item.cart_product_quantity
                else product_quantity
            )
            cart_item.cart_sub_total = (
                cart_item.cart_product_quantity * cart_item.cart_product.product_price
            )
            cart_item.save()

        else:
            raise Http404

        # Save cart totals

        return custom_redirect("cart-view", None, product_id=product_id)

    else:
        return custom_redirect("core-signup", None, next=current_url)


@wyvern_core
def cart_checkout(request):

    # TODO: Single Page Checkout or Configurable Checkout

    # Currently we will redirect them to checkout page

    return redirect("checkout-address")


@wyvern_core
def cart_remove(request):

    if request.user.is_authenticated:
        # Detect if user has a pending/uncompleted cart
        cart, created = WyvernCart.objects.get_or_create(
            cart_customer=request.user, cart_status="current"
        )

        product_id = request.GET.get("product_id") or redirect(
            "/"
        )  # TODO: Handle error

        if cart:
            cart_item = WyvernCartItem.objects.filter(
                cart_cart=cart, cart_product_id=product_id
            ).delete()

        else:
            raise Http404

        # Save cart totals

        return custom_redirect("cart-view", None, None)

    else:
        return custom_redirect("core-signup", None, next=current_url)


@wyvern_core
def cart_view(request):

    site = WyvernSite.objects.filter(site_url=request.site_url).first()
    site_template = "themes/{}/shop/cart/pages/index.html".format(site.site_template)

    return render(request, site_template, {"site": site, "page": "shopping-cart"})


def cart_update(request):

    current_url = request.get_full_path()

    if request.user.is_authenticated:
        # Detect if user has a pending/uncompleted cart
        cart, created = WyvernCart.objects.get_or_create(
            cart_customer=request.user, cart_status="current"
        )

        counter = 0

        while counter < int(request.POST.get("cart_item_count")):
            product_id = (
                request.POST.get("product_id[{}]".format(str(counter))) or 0
            )  # TODO: Handle error
            product_quantity = (
                request.POST.get("product_quantity[{}]".format(str(counter))) or 0
            )  # TODO: Handle error
            product = get_object_or_404(WyvernProduct.objects.filter(pk=product_id))

            if cart and product_id:
                cart_item = WyvernCartItem.objects.filter(
                    cart_cart=cart, cart_product_id=product_id
                ).first()

                # Update the quantity
                if product_quantity:
                    cart_item.cart_product_quantity = (
                        request.POST.get("product_quantity[{}]".format(str(counter)))
                        or 0
                    )
                    cart_item.cart_sub_total = (
                        cart_item.cart_product_quantity
                        * cart_item.cart_product.product_price
                    )
                    cart_item.save()
                else:
                    cart_item.delete()

            else:
                raise Http404

            counter += 1

        return custom_redirect("cart-view", None, product_id=product_id)

    else:
        return custom_redirect("core-signup", None, next=current_url)


def cart_delete(request):

    cart = WyvernCart.objects.filter(
        cart_customer=request.user, cart_status="current"
    ).delete()

    return redirect("cart-view")
