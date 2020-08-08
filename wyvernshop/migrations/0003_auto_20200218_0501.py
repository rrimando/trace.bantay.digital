# Generated by Django 2.0.5 on 2020-02-18 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wyvernshop", "0002_auto_20200218_0501"),
        ("wyvernsite", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wyvernshippingaddress",
            name="shipping_address_customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wyvernshippingaddress",
            name="shipping_address_site",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernsite.WyvernSite",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproducttypeconfigoption",
            name="product_type_config_option",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductTypeConfig",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproducttypeconfig",
            name="product_type_config_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductType",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproducttype",
            name="product_type_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernsite.WyvernSite"
            ),
        ),
        migrations.AddField(
            model_name="wyvernproductconfig",
            name="product_config_option",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductTypeConfig",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproductconfig",
            name="product_config_option_value",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductTypeConfigOption",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproductcategory",
            name="product_category_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernsite.WyvernSite"
            ),
        ),
        migrations.AddField(
            model_name="wyvernproductcategory",
            name="product_parent_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductCategory",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproductcategories",
            name="product_categories_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductCategory",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproductcategories",
            name="product_categories_product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProduct",
            ),
        ),
        migrations.AddField(
            model_name="wyvernproduct",
            name="product_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernsite.WyvernSite"
            ),
        ),
        migrations.AddField(
            model_name="wyvernproduct",
            name="product_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProductType",
            ),
        ),
        migrations.AddField(
            model_name="wyvernpaymentmethod",
            name="payment_method_site",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernsite.WyvernSite",
            ),
        ),
        migrations.AddField(
            model_name="wyvernpayment",
            name="payment_customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wyvernpayment",
            name="payment_method",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernPaymentMethod",
            ),
        ),
        migrations.AddField(
            model_name="wyvernpayment",
            name="payment_order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernshop.WyvernOrder"
            ),
        ),
        migrations.AddField(
            model_name="wyvernpayment",
            name="payment_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernsite.WyvernSite"
            ),
        ),
        migrations.AddField(
            model_name="wyvernorderproducts",
            name="order_product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProduct",
            ),
        ),
        migrations.AddField(
            model_name="wyvernorder",
            name="order_address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernShippingAddress",
            ),
        ),
        migrations.AddField(
            model_name="wyvernorder",
            name="order_cart",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernCart",
            ),
        ),
        migrations.AddField(
            model_name="wyvernorder",
            name="order_customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wyvernorder",
            name="order_payment_method",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernPaymentMethod",
            ),
        ),
        migrations.AddField(
            model_name="wyvernorder",
            name="order_shipping_method",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernShippingMethod",
            ),
        ),
        migrations.AddField(
            model_name="wyverninventory",
            name="inventory_product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProduct",
            ),
        ),
        migrations.AddField(
            model_name="wyverninventory",
            name="inventory_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernsite.WyvernSite"
            ),
        ),
        migrations.AddField(
            model_name="wyverncartitem",
            name="cart_cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernshop.WyvernCart"
            ),
        ),
        migrations.AddField(
            model_name="wyverncartitem",
            name="cart_product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernshop.WyvernProduct",
            ),
        ),
        migrations.AddField(
            model_name="wyverncart",
            name="cart_customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="wyverncart",
            name="cart_site",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernsite.WyvernSite",
            ),
        ),
    ]
