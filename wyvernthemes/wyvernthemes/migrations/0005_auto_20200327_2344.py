# Generated by Django 2.0.5 on 2020-03-27 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernthemes", "0004_auto_20200327_1147"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wyvernthemesite", name="wyverntheme_site_site",
        ),
        migrations.RemoveField(
            model_name="wyvernthemesite", name="wyverntheme_site_theme",
        ),
        migrations.AddField(
            model_name="wyvernthemeconfig",
            name="wyverntheme_theme",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wyvernsite_theme",
                to="wyvernthemes.WyvernTheme",
            ),
        ),
        migrations.AlterField(
            model_name="wyvernthemeconfig",
            name="wyverntheme_site",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wyvernsite_theme",
                to="wyvernsite.WyvernSite",
            ),
        ),
        migrations.DeleteModel(name="WyvernThemeSite",),
    ]
