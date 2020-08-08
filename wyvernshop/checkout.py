from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from wyvern.util.url import custom_redirect
from wyvern.util.chidori import wyvern_core
from wyvern.util.string import file_slug

from wyvernsite.models import WyvernSite
from wyvernshop.models import (
    WyvernShippingAddress,
    WyvernProduct,
    WyvernShippingMethod,
    WyvernPaymentMethod,
    WyvernOrder,
    WyvernOrderProducts,
    WyvernCart,
    WyvernCartItem,
    WyvernPayment,
)

from wyvernshop.forms import WyvernShippingAddressForm


@wyvern_core
def checkout_address(request):

    current_url = request.get_full_path()

    # TODO: Move this to a better place
    cart = WyvernCart.objects.filter(
        cart_customer=request.user, cart_status="current"
    ).first()

    if cart is None:
        messages.add_message(request, messages.INFO, "There are no items in your cart")
        return redirect("core-index")

    if request.user.is_authenticated:
        if request.POST:
            form = WyvernShippingAddressForm(request.POST)

            if form.is_valid():
                # Save the address
                shipping_address = form.save()
                return custom_redirect(
                    "checkout-shipping", None, shipping_address=shipping_address.id
                )

        else:
            form = WyvernShippingAddressForm(
                initial={
                    "shipping_address_site": request.site,
                    "shipping_address_customer": request.user,
                }
            )

        return render(
            request,
            "themes/{}/shop/checkout/pages/checkout.html".format(
                request.site.site_template
            ),
            {
                "template_action": "themes/{}/shop/checkout/partials/address.html".format(
                    request.site.site_template
                ),
                "site": request.site,
                "form": form,
                "page": "checkout-address",
            },
        )

    else:
        return custom_redirect("core-signup", None, next=current_url)


@wyvern_core
def checkout_shipping(request):

    # TODO: Move this to a better place
    cart = WyvernCart.objects.filter(
        cart_customer=request.user, cart_status="current"
    ).first()

    if cart is None:
        messages.add_message(request, messages.INFO, "There are no items in your cart")
        return redirect("core-index")

    cart_items = WyvernCartItem.objects.filter(cart_cart=cart).all()

    # Get the shipping address
    if request.POST or request.GET:

        shipping_address_id = (
            (request.POST.get("shipping_address"))
            if request.POST
            else request.GET.get("shipping_address")
        )
        shipping_address = WyvernShippingAddress.objects.filter(
            pk=shipping_address_id
        ).first()

        if shipping_address_id:

            # Create order
            order = WyvernOrder(
                order_customer=cart.cart_customer,
                order_address=shipping_address,
                order_cart=cart,
                order_status="select_shipping_method",
            )

            order.save()

            # Create order items
            for cart_item in cart_items:
                order_item = WyvernOrderProducts(
                    order_product=cart_item.cart_product,
                    order_quantity=cart_item.cart_product_quantity,
                    order_amount=cart_item.cart_product_quantity
                    * cart_item.cart_product.product_price,
                )
                order_item.save()

                order.order_amount += order_item.order_amount

            order.save()

    return render(
        request,
        "themes/{}/shop/checkout/pages/checkout.html".format(
            request.site.site_template
        ),
        {
            "template_action": "themes/{}/shop/checkout/partials/shipping.html".format(
                request.site.site_template
            ),
            "site": request.site,
            "page": "checkout-address",
        },
    )


@wyvern_core
def checkout_payment(request):
    # TODO: Move this to a better place
    cart = WyvernCart.objects.filter(
        cart_customer=request.user, cart_status="current"
    ).first()

    if cart is None:
        messages.add_message(request, messages.INFO, "There are no items in your cart")
        return redirect("core-index")

    # Get the payment method
    if request.POST or request.GET:

        shipping_method_id = (
            (request.POST.get("shipping_method"))
            if request.POST
            else request.GET.get("shipping_method")
        )
        shipping_method = WyvernShippingMethod.objects.filter(
            pk=shipping_method_id
        ).first()

        if shipping_method_id:
            # Update order
            order = WyvernOrder.objects.filter(order_cart=cart).first()
            order.order_shipping_method = shipping_method
            order.order_status = "select_payment_method"
            order.save()

    return render(
        request,
        "themes/{}/shop/checkout/pages/checkout.html".format(
            request.site.site_template
        ),
        {
            "template_action": "themes/{}/shop/checkout/partials/payment.html".format(
                request.site.site_template
            ),
            "site": request.site,
            "page": "checkout-address",
        },
    )


@wyvern_core
def checkout_process_payment(request):
    # TODO: Move this to a better place
    cart = WyvernCart.objects.filter(
        cart_customer=request.user, cart_status="current"
    ).first()

    if not cart:
        messages.add_message(request, messages.INFO, "There are no items in your cart")
        return redirect("core-index")

    # Get the payment method
    if request.POST or request.GET:

        payment_method_id = (
            (request.POST.get("payment_method"))
            if request.POST
            else request.GET.get("payment_method")
        )
        payment_method = WyvernPaymentMethod.objects.filter(
            pk=payment_method_id
        ).first()

        if payment_method_id:
            # Update order
            order = WyvernOrder.objects.filter(order_cart=cart).first()
            order.order_payment_method = payment_method
            order.order_status = "payment_pending"
            order.save()

            # Get Payment Method Details
            payment_method_id = (
                (request.POST.get("payment_method"))
                if request.POST
                else request.GET.get("payment_method")
            )
            payment_method = WyvernPaymentMethod.objects.filter(
                pk=payment_method_id
            ).first()

            # Fetch Associated Modules
            payment_method_slug = file_slug(payment_method.payment_method_name)
            payment_module = __import__(
                "wyvernshop.process_payments." + payment_method_slug,
                fromlist=[payment_method_slug],
            )
            payment_valid = payment_module.run()

            if payment_valid:

                # Update Order Status
                order.order_status = "payment_complete"
                order.save()

                # Create Payment
                payment = WyvernPayment(
                    payment_site=request.site,
                    payment_customer=request.user,
                    payment_amount=order.order_amount,
                    payment_method=order.order_payment_method,
                    payment_status="completed",
                    payment_order=order,
                )

                payment.save()

                # Update The Cart
                cart.cart_status = "completed"
                cart.save()

                # TODO: Send an Email

                # return HttpResponse("Payment was valid")
                return redirect("checkout-complete")
            else:
                order.order_status = "payment_declined"
                order.save()

    return HttpResponse("There was an error processing your payment")


@wyvern_core
def checkout_complete(request):

    return render(
        request,
        "themes/{}/shop/checkout/pages/checkout.html".format(
            request.site.site_template
        ),
        {
            "template_action": "themes/{}/shop/checkout/partials/complete.html".format(
                request.site.site_template
            ),
            "site": request.site,
            "page": "checkout-address",
        },
    )


# TODO
@wyvern_core
def checkout_update(request):
    """ Create and Process Order Here """
    pass


@wyvern_core
def checkout_single_page(request):

    return render(
        request,
        "themes/{}/shop/checkout/pages/checkout.html".format(
            request.site.site_template
        ),
        {
            "template_action": "themes/{}/shop/checkout/partials/single-page.html".format(
                request.site.site_template
            ),
            "site": request.site,
            "page": "checkout-address",
        },
    )


"""EOF"""
