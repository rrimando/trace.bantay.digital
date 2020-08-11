# Generated by Django 2.0.5 on 2020-08-09 14:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wyvernuser', '0002_auto_20200803_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True),
        ),
    ]