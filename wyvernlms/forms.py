from django import forms
from wyvernlms.models import WyvernLMSStudent


class DateInput(forms.DateInput):
    input_type = "date"


class WyvernLMSStudentForm(forms.ModelForm):
    class Meta:
        model = WyvernLMSStudent
        exclude = []

        widgets = {
            "wyvernlms_wyvern_site": forms.HiddenInput(),
            "wyvernlms_wyvern_user": forms.HiddenInput(),
            "wyvernlms_birthdate": DateInput(),
        }

        labels = {
            "wyvernlms_firstname": "First Name",
            "wyvernlms_middlename": "Middle Name",
            "wyvernlms_lastname": "Last Name",
            "wyvernlms_birthdate": "Birthdate",
            "wyvernlms_gender": "Gender",
            "wyvernlms_email_address": "Email Address",
            "wyvernlms_mobile_number": "Mobile Number",
            "wyvernlms_prev_school": "Previous School",
            "wyvernlms_year_graduated": "Year Graduated",
        }
