# Generated by Django 2.1.8 on 2020-09-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyvernuser', '0004_auto_20200819_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
