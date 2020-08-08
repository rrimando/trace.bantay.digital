# Generated by Django 2.0.5 on 2020-06-05 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernjobs", "0020_auto_20200603_0315"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wyvernjobapplicant",
            name="job_applicant_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wyvernuser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
