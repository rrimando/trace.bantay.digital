# Generated by Django 2.0.5 on 2020-02-18 05:01

from django.db import migrations, models
import django.db.models.deletion
import wyvern.util.upload


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WyvernModule",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("module_name", models.CharField(max_length=255)),
                ("module_slug", models.CharField(max_length=50)),
                ("module_description", models.TextField()),
                (
                    "module_status",
                    models.IntegerField(choices=[(0, "inactive"), (1, "active")]),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WyvernModuleConfigOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("module_config_option_name", models.CharField(max_length=20)),
                (
                    "module_config_option_validation",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "module_config_option_values",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "module_config_option_default",
                    models.TextField(blank=True, null=True),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WyvernSite",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_url", models.CharField(max_length=255, unique=True)),
                ("site_name", models.CharField(max_length=255)),
                (
                    "site_analytics",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "site_subtitle",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "site_logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=wyvern.util.upload.get_file_path,
                    ),
                ),
                (
                    "site_status",
                    models.IntegerField(choices=[(0, "inactive"), (1, "active")]),
                ),
                (
                    "site_type",
                    models.CharField(
                        choices=[
                            ("blog", "Blog"),
                            ("shop", "Shop"),
                            ("hybrid", "Hybrid"),
                        ],
                        default="blog",
                        max_length=10,
                    ),
                ),
                (
                    "site_template",
                    models.CharField(
                        choices=[
                            ("aggro", "Aggro"),
                            ("midrange", "Mid Range"),
                            ("taxproblem", "Tax Problem"),
                            ("control", "Control"),
                            ("parallax", "Parallax"),
                            ("debt", "Debt"),
                            ("taxproblem", "Tax Problem"),
                            ("jobscalle", "Jobs Calle Uno"),
                            ("lifeunited", "Life United"),
                        ],
                        default="aggro",
                        max_length=50,
                    ),
                ),
                (
                    "site_notifications_recipients",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "site_notifications_from",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("site_description", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WyvernSiteConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("config_value", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WyvernSiteConfigOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_config_option_name", models.CharField(max_length=20)),
                (
                    "site_config_option_validation",
                    models.TextField(blank=True, null=True),
                ),
                ("site_config_option_values", models.TextField(blank=True, null=True)),
                ("site_config_option_default", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WyvernSiteModuleConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_module_config_value", models.TextField(blank=True, null=True)),
                (
                    "site_module_config_module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wyvernsite.WyvernModule",
                    ),
                ),
                (
                    "site_module_config_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wyvernsite.WyvernModuleConfigOption",
                    ),
                ),
                (
                    "site_module_config_site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wyvernsite.WyvernSite",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WyvernSiteModules",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "site_module_status",
                    models.IntegerField(choices=[(0, "inactive"), (1, "active")]),
                ),
                ("date_active", models.DateTimeField(auto_now_add=True)),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wyvernsite.WyvernSite",
                    ),
                ),
                (
                    "site_module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wyvernsite.WyvernModule",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="wyvernsiteconfig",
            name="config_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="wyvernsite.WyvernSiteConfigOption",
            ),
        ),
        migrations.AddField(
            model_name="wyvernsiteconfig",
            name="config_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wyvernsite.WyvernSite"
            ),
        ),
    ]
