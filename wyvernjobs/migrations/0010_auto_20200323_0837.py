# Generated by Django 2.0.5 on 2020-03-23 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernjobs", "0009_auto_20200323_0836"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wyvernjobapplicant",
            name="job_applicant_user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wyvernuser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
