# Generated by Django 2.0.5 on 2020-08-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernthemes", "0010_auto_20200616_0309"),
    ]

    operations = [
        migrations.AddField(
            model_name="wyvernthemeconfig",
            name="wyverntheme_back_to_top",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="wyvernthemeconfig",
            name="wyverntheme_gdpr",
            field=models.BooleanField(default=False),
        ),
    ]
