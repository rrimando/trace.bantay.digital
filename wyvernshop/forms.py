from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import (
    WyvernProduct,
    WyvernProductCategory,
    WyvernProductCategories,
    WyvernShippingAddress,
    WyvernShippingMethod,
    WyvernPaymentMethod,
)

from ckeditor_uploader.widgets import CKEditorUploadingWidget

"""
    TODO: https://stackoverflow.com/questions/12144475/displaying-multiple-rows-and-columns-in-django-crispy-forms
"""


class WyvernProductForm(forms.ModelForm):

    product_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = WyvernProduct
        exclude = []
        widgets = {
            "product_name": forms.TextInput(
                attrs={
                    "class": "form-control slugify",
                    "data-target": "#id_product_slug",
                }
            ),
            "product_site": forms.HiddenInput(),
        }


class WyvernProductCategoryForm(forms.ModelForm):

    product_category_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = WyvernProductCategory
        exclude = []
        widgets = {
            "product_category_name": forms.TextInput(
                attrs={
                    "class": "form-control slugify",
                    "data-target": "#id_product_category_slug",
                }
            ),
            "product_category_site": forms.HiddenInput(),
        }


class WyvernProductCategoriesForm(forms.ModelForm):
    class Meta:
        model = WyvernProductCategories
        exclude = []
        widgets = {"product_categories_product": forms.HiddenInput()}


class WyvernShippingAddressForm(forms.ModelForm):
    class Meta:
        model = WyvernShippingAddress
        exclude = []

        widgets = {
            "shipping_address_site": forms.HiddenInput(),
            "shipping_address_customer": forms.HiddenInput(),
        }

        labels = {
            "shipping_address_first_name": "Firstname",
            "shipping_address_last_name": "Lastname",
            "shipping_address_contact_no": "Contact Number",
            "shipping_address_email_notifications": "Email",
            "shipping_address_address_line_1": "Address Line 1",
            "shipping_address_address_line_2": "Address Line 2",
            "shipping_address_city": "City",
            "shipping_address_state": "State",
            "shipping_address_country": "Country",
            "shipping_address_postcode": "Postal Code",
            "shipping_address_default": "Default shipping address",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ LAYOUT """
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    "shipping_address_first_name", css_class="form-group col-md-6 mb-0"
                ),
                Column(
                    "shipping_address_last_name", css_class="form-group col-md-6 mb-0"
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "shipping_address_contact_no", css_class="form-group col-md-6 mb-0"
                ),
                Column(
                    "shipping_address_email_notifications",
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            "shipping_address_address_line_1",
            "shipping_address_address_line_2",
            Row(
                Column("shipping_address_city", css_class="form-group col-md-3 mb-0"),
                Column("shipping_address_state", css_class="form-group col-md-3 mb-0"),
                Column(
                    "shipping_address_country", css_class="form-group col-md-3 mb-0"
                ),
                Column(
                    "shipping_address_postcode", css_class="form-group col-md-3 mb-0"
                ),
                css_class="form-row",
            ),
            "shipping_address_default",
            "shipping_address_site",
            "shipping_address_customer",
            Submit("submit", "Continue"),
        )


class WyvernShippingMethodForm(forms.ModelForm):
    class Meta:
        model = WyvernShippingMethod
        exclude = []
        widgets = {"shipping_method_site": forms.HiddenInput()}


class WyvernPaymentMethodForm(forms.ModelForm):
    class Meta:
        model = WyvernPaymentMethod
        exclude = []
        widgets = {
            "payment_method_site": forms.HiddenInput(),
            "payment_method_configuration": forms.HiddenInput(),
        }
