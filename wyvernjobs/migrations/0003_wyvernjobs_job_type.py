# Generated by Django 2.0.5 on 2020-02-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernjobs", "0002_auto_20200218_0501"),
    ]

    operations = [
        migrations.AddField(
            model_name="wyvernjobs",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("general", "General"),
                    ("it", "Information Technology and Service"),
                    ("hr", "Human Resources"),
                    ("cs", "Customer Support"),
                    ("va", "Virtual Assistance"),
                    ("marketing", "Marketing and Advertising"),
                ],
                default="general",
                max_length=50,
            ),
        ),
    ]
