from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from wyvernuser.models import User
from wyverntrace.models import WyvernMedicalForm, WyvernTraceLog

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class WyvernTraceLogForm(forms.ModelForm):
    class Meta:
        model = WyvernTraceLog
        fields = "__all__"
        labels = {
            "wyvern_first_name": "Resident First Name",
            "wyvern_last_name": "Resident Last Name",
            "wyvern_phone_number": "Resident Phone Number",
            "wyvern_resident_address": "Resident Address",
            "wyvern_temperature": "Resident Temperature",
        }
        widgets = {
            "wyvern_user": forms.HiddenInput(),
            "wyvern_location": forms.HiddenInput(),
            "wyvern_first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "wyvern_last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "wyvern_phone_number": forms.TextInput(
                attrs={"placeholder": "Phone Number"}
            ),
            "wyvern_temperature": forms.TextInput(attrs={"placeholder": "Temperature"}),
            "wyvern_resident_address": forms.Textarea(
                attrs={"placeholder": "Resident Full Address", "rows": 5}
            ),
        }


class WyvernMedicalForms(forms.ModelForm):
    class Meta:
        model = WyvernMedicalForm
        fields = "__all__"
        exclude = ["wyvern_medical_form_date"]

        labels = {
            "wyvern_have_sore_throat": "Do you have a sore throat?",
            "wyvern_have_body_pain": "Are you experiencing any body pain?",
            "wyvern_have_head_ache": "Do you have a head throat?",
            "wyvern_have_fever": "Do you have a fever?",
            "wyvern_near_covid": "Have you been in contact with any diagnosed with COVID19?",
            "wyvern_contact_symptoms": "Have you been in contact with anyone showing any symptoms of COVID19?",
            "wyvern_travelled_outside_philippines": "Have you recently travelled outside the Philippines?",
            "wyvern_travelled_ncr": "Have you recently travelled to the National Capital Region?",
        }

        widgets = {
            "wyvern_medical_form_user": forms.HiddenInput(),
        }


class WyvernResidentForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
    )

    class Meta:

        # TODO: https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms

        model = User
        exclude = [
            "user_permissions",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "about",
            "date_joined",
            "groups",
            "image",
            "hometown",
            "location",
            "geolocation",
            "facebook",
            "website",
            "gender",
            "interests",
            "is_location",
            "uuid",
            "resident_establishment_filter",
        ]
        labels = {
            "email": "Email/Username",
            "accepted_terms": 'I have read and accept the <a href="/page/terms-and-conditions/">Terms and Conditions</a>',
        }
        widgets = {
            "username": forms.HiddenInput(),
            "site_id": forms.HiddenInput(),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email Address"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "address": forms.Textarea(attrs={"placeholder": "Full Address", "rows": 5}),
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2


class WyvernResidentDetailsForm(forms.ModelForm):
    class Meta:

        # TODO: https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms

        model = User
        exclude = [
            "user_permissions",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "about",
            "date_joined",
            "groups",
            "image",
            "hometown",
            "location",
            "geolocation",
            "facebook",
            "website",
            "gender",
            "interests",
            "is_location",
            "uuid",
            "password",
            "confirm_password",
            "resident_establishment_filter",
        ]
        labels = {
            "email": "Email/Username",
            "accepted_terms": 'I have read and accept the <a href="/page/terms-and-conditions/">Terms and Conditions</a>',
        }
        widgets = {
            "username": forms.HiddenInput(),
            "site_id": forms.HiddenInput(),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email Address"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "address": forms.Textarea(attrs={"placeholder": "Full Address", "rows": 5}),
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2


class WyvernEstablishmentForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
    )
    is_location = forms.BooleanField(initial=True)

    class Meta:

        # TODO: https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms

        model = User
        exclude = [
            "user_permissions",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "about",
            "date_joined",
            "groups",
            "image",
            "hometown",
            "location",
            "geolocation",
            "facebook",
            "website",
            "gender",
            "interests",
            "resident_establishment_filter",
        ]
        labels = {
            "first_name": "Establishment Name",
            "last_name": "Contact Person",
            "accepted_terms": 'I have read and accept the <a href="/page/terms-and-conditions/">Terms and Conditions</a>.',
        }
        widgets = {
            "site_id": forms.HiddenInput(),
            "is_location": forms.HiddenInput(),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "first_name": forms.TextInput(attrs={"placeholder": "Establishment Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Contact Person"}),
            "email": forms.TextInput(attrs={"placeholder": "Email Address"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "address": forms.Textarea(attrs={"placeholder": "Full Address", "rows": 5}),
        }


class WyvernEstablishmentDetailsForm(forms.ModelForm):
    class Meta:

        # TODO: https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms

        model = User
        exclude = [
            "user_permissions",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "about",
            "date_joined",
            "groups",
            "image",
            "hometown",
            "location",
            "geolocation",
            "facebook",
            "website",
            "gender",
            "interests",
            "uuid",
            "password",
            "confirm_password",
            "resident_establishment_filter",
        ]
        labels = {
            "first_name": "Establishment Name",
            "last_name": "Contact Person",
            "accepted_terms": 'I have read and accept the <a href="/page/terms-and-conditions/">Terms and Conditions</a>.',
        }
        widgets = {
            "username": forms.HiddenInput(),
            "site_id": forms.HiddenInput(),
            "is_location": forms.HiddenInput(),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "first_name": forms.TextInput(attrs={"placeholder": "Establishment Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Contact Person"}),
            "email": forms.TextInput(attrs={"placeholder": "Email Address"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "address": forms.Textarea(attrs={"placeholder": "Full Address", "rows": 5}),
        }
