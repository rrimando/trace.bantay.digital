from django import forms
from wyvernblog.models import WyvernPost

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class WyvernPostForm(forms.ModelForm):
    post_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = WyvernPost
        exclude = []
        widgets = {
            "post_title": forms.TextInput(
                attrs={"class": "form-control slugify", "data-target": "#id_post_slug"}
            ),
            "post_site": forms.HiddenInput(),
        }
