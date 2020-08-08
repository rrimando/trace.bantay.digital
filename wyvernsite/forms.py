from django import forms
from .models import WyvernSite


class WyvernSiteForm(forms.ModelForm):
    class Meta:
        model = WyvernSite
        exclude = []
