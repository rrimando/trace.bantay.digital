"""
    Wyvern Shop Context 
"""
from .models import (
    WyvernProduct,
    WyvernCart,
    WyvernCartItem,
    WyvernShippingAddress,
    WyvernShippingMethod,
    WyvernPaymentMethod,
    WyvernProductCategory,
)


def products(request):

    try:
        request.site
    except AttributeError:
        products = None
    else:
        products = WyvernProduct.objects.filter(product_site=request.site).all()

    return {"products": products}


def product_categories(request):

    try:
        request.site
    except AttributeError:
        product_categories = None
    else:
        product_categories = WyvernProductCategory.objects.filter(
            product_category_site=request.site
        ).all()

    return {"product_categories": product_categories}


def cart(request):

    cart = None
    cart_items = None

    try:
        request.site
    except AttributeError:
        cart = None
    else:
        if request.user.is_authenticated:
            cart, created = WyvernCart.objects.get_or_create(
                cart_customer=request.user, cart_status="current"
            )
            cart_items = WyvernCartItem.objects.filter(cart_cart=cart).all()

            cart.cart_total = 0

            for cart_item in cart_items:
                cart.cart_total += cart_item.cart_sub_total

            cart.save()

    return {
        "cart": cart,
        "cart_items": cart_items,
        "cart_total": cart.cart_total if cart else None,
    }


def addresses(request):

    try:
        request.site
    except AttributeError:
        shipping_addresses = None
    else:
        if request.user.is_authenticated:
            shipping_addresses = WyvernShippingAddress.objects.filter(
                shipping_address_customer=request.user
            )
        else:
            shipping_addresses = None

    return {"shipping_addresses": shipping_addresses}


def shipping_methods(request):

    try:
        request.site
    except AttributeError:
        shipping_methods = None
    else:
        if request.user.is_authenticated:
            shipping_methods = WyvernShippingMethod.objects.filter(
                shipping_method_site=request.site, shipping_method_enabled=True
            ).all()
        else:
            shipping_methods = None

    return {"shipping_methods": shipping_methods}


def payment_methods(request):

    try:
        request.site
    except AttributeError:
        payment_methods = None
    else:
        if request.user.is_authenticated:
            payment_methods = WyvernPaymentMethod.objects.filter(
                payment_method_site=request.site, payment_method_enabled=True
            ).all()
        else:
            payment_methods = None

    return {"payment_methods": payment_methods}
