# Generated by Django 2.0.5 on 2020-06-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernblog", "0005_auto_20200324_0724"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wyvernpost",
            name="post_slug",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]