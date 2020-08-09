from django import forms
from wyvernuser.models import User

from ckeditor_uploader.widgets import CKEditorUploadingWidget


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
        ]
        widgets = {
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
            'first_name': 'Establishment Name',
            'last_name': 'Contact Person'
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