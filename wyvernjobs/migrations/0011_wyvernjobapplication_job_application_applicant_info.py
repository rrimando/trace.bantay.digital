# Generated by Django 2.0.5 on 2020-03-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernjobs", "0010_auto_20200323_0837"),
    ]

    operations = [
        migrations.AddField(
            model_name="wyvernjobapplication",
            name="job_application_applicant_info",
            field=models.ManyToManyField(
                related_name="wyvernapplicant", to="wyvernjobs.WyvernJobApplicant"
            ),
        ),
    ]
