from django import forms
from wyvernuser.models import User
from wyverntrace.models import WyvernMedicalForm

from ckeditor_uploader.widgets import CKEditorUploadingWidget


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


class WyvernEstablishmentForm(forms.ModelForm):
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
