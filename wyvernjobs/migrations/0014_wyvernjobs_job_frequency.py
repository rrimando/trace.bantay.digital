# Generated by Django 2.0.5 on 2020-03-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernjobs", "0013_wyvernjobs_job_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="wyvernjobs",
            name="job_frequency",
            field=models.CharField(
                choices=[("part_time", "Part Time"), ("full_time", "Full Time")],
                default="full_time",
                max_length=50,
            ),
        ),
    ]