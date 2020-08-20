# Generated by Django 3.1 on 2020-08-19 06:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wyvernuser', '0003_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True, unique=True),
        ),
    ]