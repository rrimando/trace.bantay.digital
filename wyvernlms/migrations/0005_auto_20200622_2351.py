# Generated by Django 2.0.5 on 2020-06-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wyvernlms", "0004_auto_20200622_2350"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wyvernlmsstudent",
            name="wyvernlms_birthdate",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
