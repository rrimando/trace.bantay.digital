# Generated by Django 2.0.5 on 2020-03-27 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernthemes", "0005_auto_20200327_2344"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wyvernthemeconfig",
            name="wyverntheme_site",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wyvernsite_theme_site",
                to="wyvernsite.WyvernSite",
            ),
        ),
        migrations.AlterField(
            model_name="wyvernthemeconfig",
            name="wyverntheme_theme",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wyvernsite_theme_theme",
                to="wyvernthemes.WyvernTheme",
            ),
        ),
    ]
