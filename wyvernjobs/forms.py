from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import WyvernJobs, WyvernJobApplicant, WyvernJobApplication

from ckeditor_uploader.widgets import CKEditorUploadingWidget

"""
    TODO: https://stackoverflow.com/questions/12144475/displaying-multiple-rows-and-columns-in-django-crispy-forms
"""


class WyvernJobForm(forms.ModelForm):

    job_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = WyvernJobs
        exclude = []
        widgets = {
            "job_title": forms.TextInput(
                attrs={"class": "form-control slugify", "data-target": "#id_job_slug"}
            ),
            "job_site": forms.HiddenInput(),
        }


class WyvernJobApplicantForm(forms.ModelForm):
    class Meta:
        model = WyvernJobApplicant
        exclude = []

        labels = {
            "job_applicant_title": "Current/Last Position",
            "job_applicant_firstname": "First Name",
            "job_applicant_lastname": "Last Name",
            "job_applicant_email": "Email Address",
            "job_applicant_number": "Contact Number",
            "job_applicant_introduction": "Short Intro(Optional)",
            "job_applicant_resume": "Resume",
            "job_applicant_additional_form": "Attachments",
        }
        # help_texts = {
        #     # 'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     # 'name': {
        #     #     'max_length': _("This writer's name is too long."),
        #     # },
        # }

        widgets = {
            "job_applicant_user": forms.HiddenInput(),
            "job_applicant_site": forms.HiddenInput(),
        }


class WyvernJobApplicationForm(forms.ModelForm):
    class Meta:
        model = WyvernJobApplication
        labels = {
            "job_application_cover_letter": "Cover Letter(Optional)",
        }
        exclude = []
        widgets = {
            "job_application_applicant_user": forms.HiddenInput(),
            "job_application_applicant": forms.HiddenInput(),
            "job_application_site": forms.HiddenInput(),
            "job_application_job": forms.HiddenInput(),
        }
