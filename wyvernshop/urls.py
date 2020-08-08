"""

Wyvern Shop - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Products
    path("", views.index, name="shop-index"),
    url(r"^product/list/$", views.index),
    url(
        r"^product/create/(?P<site>[-\w\d@\.-:]+)$",
        views.product_create,
        name="product-create",
    ),
    url(r"^product/edit/(?P<slug>[\w.-]+)/$", views.product_edit, name="product-edit"),
    url(r"^product/view/(?P<slug>[\w.-]+)/$", views.product_view, name="product-view"),
    url(
        r"^product/delete/(?P<slug>[\w.-]+)/$",
        views.product_delete,
        name="product-delete",
    ),
    url(r"^product/(?P<slug>[\w.-]+)/$", views.product_view, name="product-view"),
    # Product Category
    path("", views.index, name="shop-index"),
    url(r"^product-category/list/$", views.index),
    url(
        r"^product-category/create/(?P<site>[-\w\d@\.-:]+)$",
        views.product_category_create,
        name="product-category-create",
    ),
    url(
        r"^product-category/edit/(?P<slug>[\w.-]+)/$",
        views.product_category_edit,
        name="product-category-edit",
    ),
    url(
        r"^product-category/view/(?P<slug>[\w.-]+)/$",
        views.product_category_view,
        name="product-category-view",
    ),
    url(
        r"^product-category/delete/(?P<slug>[\w.-]+)/$",
        views.product_category_delete,
        name="product-category-delete",
    ),
    url(
        r"^product-category/(?P<slug>[\w.-]+)/$",
        views.product_category_view,
        name="product-category-view",
    ),
    # Cart
    url(r"^cart/add/$", views.cart_add, name="cart-add"),
    url(r"^cart/remove/$", views.cart_remove, name="cart-remove"),
    url(r"^cart/view/$", views.cart_view, name="cart-view"),
    url(r"^cart/update/$", views.cart_update, name="cart-update"),
    url(r"^cart/delete/$", views.cart_delete, name="cart-delete"),
    url(r"^cart/checkout/$", views.cart_checkout, name="cart-checkout"),
    # Checkout
    url(
        r"^checkout/update/$", views.checkout_update, name="checkout-update"
    ),  # TODO: Refactor cart and order to utilize one method
    url(r"^checkout/address/$", views.checkout_address, name="checkout-address"),
    url(r"^checkout/shipping/$", views.checkout_shipping, name="checkout-shipping"),
    url(r"^checkout/payment/$", views.checkout_payment, name="checkout-payment"),
    url(
        r"^checkout/process-payment/$",
        views.checkout_process_payment,
        name="checkout-process-payment",
    ),
    url(r"^checkout/complete/$", views.checkout_complete, name="checkout-complete"),
    # Product Types
    # Categories
    # Shipping Methods
    url(r"^shipping-method/list/$", views.index),
    url(
        r"^shipping-method/create/(?P<site>[-\w\d@\.-:]+)$",
        views.shipping_method_create,
        name="shipping-method-create",
    ),
    url(
        r"^shipping-method/edit/(?P<id>[0-9]+)/$",
        views.shipping_method_edit,
        name="shipping-method-edit",
    ),
    url(
        r"^shipping-method/view/(?P<id>[0-9]+)/$",
        views.shipping_method_view,
        name="shipping-method-view",
    ),
    url(
        r"^shipping-method/delete/(?P<id>[0-9]+)/$",
        views.shipping_method_delete,
        name="shipping-method-delete",
    ),
    # Payment Methods
    url(r"^payment-method/list/$", views.index),
    url(
        r"^payment-method/create/(?P<site>[-\w\d@\.-:]+)$",
        views.payment_method_create,
        name="payment-method-create",
    ),
    url(
        r"^payment-method/edit/(?P<id>[0-9]+)/$",
        views.payment_method_edit,
        name="payment-method-edit",
    ),
    url(
        r"^payment-method/view/(?P<id>[0-9]+)/$",
        views.payment_method_view,
        name="payment-method-view",
    ),
    url(
        r"^payment-method/delete/(?P<id>[0-9]+)/$",
        views.payment_method_delete,
        name="payment-method-delete",
    ),
    # Customers
    # Orders
]
