# Generated by Django 2.0.5 on 2020-08-03 04:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernuser", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_location",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits are allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="site_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
