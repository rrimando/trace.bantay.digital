"""

WYVERN SHOP - MODELS

Schema Design: 

TODO: https://docs.google.com/spreadsheets/d/1eps2dIHlUoAq2QI-ysHw6uhrH0vUHK_BX_yKDe6o8W0/edit#gid=0

Reference:

https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

"""
import wyvern.util.config as config

from django.db import models

# from django.contrib.auth.models import User

from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernProductType(models.Model):

    product_type_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    product_type_name = models.CharField(max_length=255)
    product_type_description = models.TextField(null=True, blank=True)


class WyvernProductTypeConfig(models.Model):

    product_type_config_type = models.ForeignKey(
        WyvernProductType, on_delete=models.CASCADE
    )
    product_type_config_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernProductTypeConfigOption(models.Model):

    product_type_config_option = models.ForeignKey(
        WyvernProductTypeConfig, on_delete=models.CASCADE
    )
    product_type_config_option_value = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernProductCategory(models.Model):

    product_category_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    product_parent_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True
    )
    product_category_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    product_category_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )
    product_category_featured_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )
    product_category_name = models.CharField(max_length=255)
    product_category_sub_text = models.CharField(max_length=255, blank=True, null=True)
    product_category_slug = models.CharField(
        max_length=255, unique=True, default="", null=True, blank=True
    )
    product_category_description = models.TextField(null=True, blank=True)
    product_category_content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.product_category_name

    def get_image_url(self):
        try:
            # or whatever causes the exception
            return self.product_category_image.url
        except ValueError:
            return None

    def get_feature_image_url(self):
        try:
            # or whatever causes the exception
            return self.product_category_featured_image.url
        except ValueError:
            return None


class WyvernProduct(models.Model):

    product_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_alt_image_1 = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )
    product_alt_image_2 = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )
    product_name = models.CharField(max_length=255)
    product_sub_text = models.CharField(max_length=255, default="")
    product_weight = models.CharField(max_length=255, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_type = models.ForeignKey(
        WyvernProductType, on_delete=models.CASCADE, blank=True, null=True
    )
    product_code = models.CharField(max_length=255, null=True, blank=True)
    product_slug = models.CharField(
        max_length=255, unique=True, default="", null=True, blank=True
    )
    product_sku = models.CharField(max_length=255, null=True, blank=True)
    product_price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    product_enabled = models.BooleanField(default=True)
    # New Fields
    product_content = models.TextField(null=True, blank=True)
    product_short_description = models.TextField(null=True, blank=True)
    product_featured_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )

    def get_image_url(self):
        try:
            # or whatever causes the exception
            return self.product_image.url
        except ValueError:
            return None

    def get_alt_image_url(self):
        try:
            # or whatever causes the exception
            return self.product_alt_image_1.url
        except ValueError:
            return None

    def get_feature_image_url(self):
        try:
            # or whatever causes the exception
            return self.product_featured_image.url
        except ValueError:
            return None


class WyvernProductCategories(models.Model):

    product_categories_product = models.ForeignKey(
        WyvernProduct, on_delete=models.CASCADE
    )
    product_categories_category = models.ForeignKey(
        WyvernProductCategory, on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernProductConfig(models.Model):

    product_config_option = models.ForeignKey(
        WyvernProductTypeConfig, on_delete=models.CASCADE
    )
    product_config_option_value = models.ForeignKey(
        WyvernProductTypeConfigOption, on_delete=models.CASCADE
    )


class WyvernInventory(models.Model):

    unit_type = [("weight", "Weight"), ("container", "Container"), ("pieces", "Pieces")]

    inventory_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    inventory_product = models.ForeignKey(WyvernProduct, on_delete=models.CASCADE)
    inventory_quantity = models.IntegerField()
    inventory_unit = models.CharField(max_length=255)
    inventory_unit_type = models.CharField(
        max_length=10, choices=unit_type, default="current"
    )  # Move to config


class WyvernCart(models.Model):

    cart_status = [
        # ('pending', 'Pending'),
        # ('expired', 'Expired'),
        # ('abandoned', 'Abandoned'),
        ("current", "Current"),
        ("completed", "Completed"),
        # ('deleted', 'Deleted'),
    ]

    cart_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, null=True, blank=True
    )
    cart_customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer"
    )
    cart_status = models.CharField(
        max_length=10, choices=cart_status, default="current"
    )
    cart_total = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", default="0"
    )
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


class WyvernCartItem(models.Model):

    cart_cart = models.ForeignKey(WyvernCart, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(WyvernProduct, on_delete=models.CASCADE)
    cart_product_quantity = models.IntegerField(default=0)
    cart_sub_total = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", default="0"
    )

    def get_product_details(self):
        return WyvernProduct.objects.filter(pk=self.cart_product.id)


class WyvernShippingAddress(models.Model):

    # TODO: Move this to WyvernUserProfile

    shipping_address_first_name = models.CharField(max_length=255, default="")
    shipping_address_last_name = models.CharField(max_length=255, default="")
    shipping_address_contact_no = models.CharField(max_length=255, default="")
    shipping_address_email_notifications = models.CharField(max_length=255, default="")
    shipping_address_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, null=True, blank=True
    )
    shipping_address_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address_address_line_1 = models.CharField(max_length=255, default="")
    shipping_address_address_line_2 = models.CharField(
        max_length=255, blank=True, null=True
    )
    shipping_address_city = models.CharField(max_length=255, default="")
    shipping_address_state = models.CharField(
        max_length=255, null=True, blank=True, default=""
    )
    shipping_address_country = CountryField(default="PH")
    shipping_address_postcode = models.CharField(max_length=255, default="")
    shipping_address_default = models.BooleanField(default=True)

    def get_address_summary(self):
        return ("{} {} - {}, {}, {}").format(
            self.shipping_address_first_name,
            self.shipping_address_last_name,
            self.shipping_address_address_line_1,
            self.shipping_address_city,
            self.shipping_address_country,
        )


class WyvernShippingProvider(models.Model):

    shipping_provider_name = models.CharField(max_length=255)
    shipping_provider_website = models.TextField(null=True, blank=True)


class WyvernShippingType(models.Model):

    shipping_method_type_provider = models.ForeignKey(
        WyvernShippingProvider, on_delete=models.CASCADE
    )
    shipping_method_type_name = models.CharField(max_length=255)
    shipping_method_type_provider = models.CharField(max_length=255)
    shipping_method_type_description = models.TextField(null=True, blank=True)


class WyvernShippingMethod(models.Model):

    shipping_method_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, null=True, blank=True
    )
    shipping_method_type = models.ForeignKey(
        WyvernShippingType, on_delete=models.CASCADE, null=True, blank=True
    )
    shipping_method_name = models.CharField(max_length=255)
    shipping_method_description = models.TextField(null=True, blank=True)
    shipping_method_cost = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD"
    )
    shipping_method_enabled = models.BooleanField(default=True)

    def get_method_summary(self):
        return "{} ({})".format(self.shipping_method_name, self.shipping_method_cost)


class WyvernPaymentMethod(models.Model):

    payment_method_site = models.ForeignKey(
        WyvernSite, on_delete=models.CASCADE, null=True, blank=True
    )
    payment_method_name = models.CharField(max_length=255)
    payment_method_provider = models.CharField(max_length=255)
    payment_method_description = models.TextField(null=True, blank=True)
    payment_method_instructions = models.TextField(null=True, blank=True)
    payment_method_configuration = models.TextField(
        null=True, blank=True
    )  # JSON/Encoded
    payment_method_enabled = models.BooleanField(default=True)

    def get_method_summary(self):
        return "{} ({})".format(self.payment_method_name, self.payment_method_provider)


class WyvernOrder(models.Model):

    order_status = [
        ("select_address", "Select Address"),
        ("select_shipping_method", "Select Shipping Method"),
        ("select_payment_method", "Select Payment Method"),
        ("payment_complete", "Payment Complete"),
        ("payment_pending", "Payment Pending"),
        ("payment_declined", "Pending Payment"),
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("for_clarification", "For Clarification"),
        ("for_shipment", "For Shipment"),
        ("shipped", "Shipped"),
        ("refunded", "Refunded"),
        ("returned", "Returned"),
        ("cancelled", "Cancelled"),
        ("deleted", "Deleted"),
        ("completed", "Completed"),
    ]

    order_cart = models.ForeignKey(
        WyvernCart, on_delete=models.CASCADE, blank=True, null=True
    )
    order_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    order_amount = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", default=0
    )
    order_address = models.ForeignKey(WyvernShippingAddress, on_delete=models.CASCADE)
    order_shipping_method = models.ForeignKey(
        WyvernShippingMethod,
        on_delete=models.CASCADE,
        default="",
        blank=True,
        null=True,
    )
    order_payment_method = models.ForeignKey(
        WyvernPaymentMethod, on_delete=models.CASCADE, default="", blank=True, null=True
    )
    order_status = models.CharField(
        max_length=25, choices=order_status, default="select_address"
    )


class WyvernOrderProducts(models.Model):

    order_product = models.ForeignKey(WyvernProduct, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    order_amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")


class WyvernPayment(models.Model):

    payment_status = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("declined", "Declined"),
    ]

    payment_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    payment_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    payment_method = models.ForeignKey(WyvernPaymentMethod, on_delete=models.CASCADE)
    payment_status = models.CharField(
        max_length=10, choices=payment_status, default="current"
    )
    payment_order = models.ForeignKey(WyvernOrder, on_delete=models.CASCADE)
