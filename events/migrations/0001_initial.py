# Generated by Django 5.0.4 on 2024-05-27 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organizer", "0001_initial"),
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=200)),
                ("date", models.DateField(default="2019-01-01")),
                (
                    "location",
                    models.CharField(default="default location", max_length=200),
                ),
                ("description", models.TextField(default="default description")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="プロフィール画像",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "下書き"), ("published", "公開済み")],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("is_finished", models.BooleanField(default=False)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("festival", "祭り"),
                            ("concert", "コンサート"),
                            ("sports", "スポーツ"),
                            ("other", "その他"),
                        ],
                        default="festival",
                        max_length=10,
                    ),
                ),
                (
                    "organizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizer.organizerprofile",
                    ),
                ),
                (
                    "vendors",
                    models.ManyToManyField(
                        blank=True, related_name="vendors", to="vendor.vendorprofile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField(default="default message")),
                ("is_approved", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="events.event",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="vendor.vendorprofile",
                    ),
                ),
            ],
        ),
    ]
