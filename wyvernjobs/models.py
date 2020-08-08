"""

WYVERN SITE JOBS - MODELS

Schema Design: TODO

https://docs.google.com/spreadsheets/d/1eps2dIHlUoAq2QI-ysHw6uhrH0vUHK_BX_yKDe6o8W0/edit#gid=0

Reference:

https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

"""
import wyvern.util.config as config

from django.db import models

# from django.contrib.auth.models import User

from wyvern.util.array import choices
from wyvern.util.upload import get_file_path

from wyvernuser.models import User
from wyvernsite.models import WyvernSite
from wyvernutilities.models import Status


class WyvernJobs(models.Model):

    job_types = [
        ("general", "General"),
        ("it", "Information Technology and Service"),
        ("hr", "Human Resources"),
        ("cs", "Customer Support"),
        ("va", "Virtual Assistance"),
        ("ck", "Cleaning / Kitchen"),
        ("hca", "Health Care Assistant"),
        ("nurse", "Nurse"),
        ("sw", "Support Workers"),
        ("marketing", "Marketing and Advertising"),
    ]

    job_hour_options = [
        ("Temporary", "Temporary"),
        ("Agency Staffing", "Agency Staffing"),
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time"),
        ("Part Time / Full Time", "Part Time / Full Time"),
        ("Project Based", "Project Based"),
    ]

    job_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField(null=True, blank=True)
    job_subtitle = models.CharField(max_length=255, null=True, blank=True)
    job_slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    job_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )  # TODO - Pull from config
    job_status = models.IntegerField(choices=choices(Status))
    job_posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_experience_required = models.CharField(max_length=255, default="Entry Level")
    job_content = models.TextField(null=True, blank=True)
    job_location = models.CharField(
        max_length=255, default="Baguio City"
    )  # Pull from config
    job_hours = models.CharField(
        max_length=100, choices=job_hour_options, default="Full Time"
    )  # Pull from config
    job_type = models.CharField(
        max_length=100, choices=job_types, default="general"
    )  # Pull from config
    job_notifications_recipients = models.CharField(
        max_length=255, null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Job: {} ({})".format(self.job_title, self.job_site.job_site_url)


# Job Types
class WyvernJobTypes(models.Model):
    # Basic Part Time, Full Time
    job_type_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_type_title = models.CharField(max_length=255)


# Job Categories
class WyvernJobCategories(models.Model):
    job_category_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_category_title = models.CharField(max_length=255)
    job_category_description = models.TextField(null=True, blank=True)
    job_category_short_description = models.CharField(
        max_length=255, null=True, blank=True
    )
    job_category_parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    job_category_slug = models.CharField(max_length=255, null=True, blank=True)
    job_category_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )  # TODO - Pull from config
    job_category_status = models.IntegerField(choices=choices(Status))
    job_category_content = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


# Job Applicant
class WyvernJobApplicant(models.Model):
    job_applicant_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wyvernuser", null=True, blank=True
    )
    job_applicant_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_applicant_firstname = models.CharField(max_length=255, null=True, blank=True)
    job_applicant_lastname = models.CharField(max_length=255, null=True, blank=True)
    job_applicant_title = models.CharField(max_length=255, null=True, blank=True)
    job_applicant_email = models.CharField(max_length=255, null=True, blank=True)
    job_applicant_number = models.CharField(max_length=255, null=True, blank=True)
    job_applicant_resume = models.FileField(
        upload_to=get_file_path, null=True, blank=True
    )
    job_applicant_additional_form = models.FileField(
        upload_to=get_file_path, null=True, blank=True
    )


# Job Employer
class WyvernEmployer(models.Model):
    job_employer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_employer_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_employer_title = models.TextField(null=True, blank=True)
    job_employer_company_name = models.TextField(null=True, blank=True)
    job_employer_company_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True
    )  # TODO - Pull from config


class WyvernEmployerJobs(models.Model):
    job_employer_jobs_employer = models.ForeignKey(
        WyvernEmployer, on_delete=models.CASCADE
    )
    job_employer_jobs_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_employer_jobs_job = models.ForeignKey(WyvernJobs, on_delete=models.CASCADE)


# Job Applications
class WyvernJobApplication(models.Model):
    job_application_applicant_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    job_application_applicant = models.ForeignKey(
        WyvernJobApplicant, on_delete=models.CASCADE, null=True, blank=True
    )
    job_application_site = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    job_application_job = models.ForeignKey(WyvernJobs, on_delete=models.CASCADE)
    job_application_cover_letter = models.TextField(null=True, blank=True)


"""Wyvern Jobs Models EOF"""
