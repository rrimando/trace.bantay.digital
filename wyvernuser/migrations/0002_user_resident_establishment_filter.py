# Generated by Django 3.1 on 2020-09-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyvernuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resident_establishment_filter',
            field=models.TextField(blank=True, null=True),
        ),
    ]
