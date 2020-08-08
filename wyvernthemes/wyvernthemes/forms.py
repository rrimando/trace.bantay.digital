from django import forms

from .models import WyvernThemeConfig

"""
    TODO: https://stackoverflow.com/questions/12144475/displaying-multiple-rows-and-columns-in-django-crispy-forms
"""


class WyvernThemeConfigForm(forms.ModelForm):
    class Meta:
        model = WyvernThemeConfig
        exclude = []
        widgets = {"wyverntheme_site": forms.HiddenInput()}
