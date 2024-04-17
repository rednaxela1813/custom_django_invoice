# Generated by Django 4.2.7 on 2024-04-17 13:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("phone", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientPrivatPerson",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("ICO", models.CharField(blank=True, max_length=10, null=True)),
                ("DIC", models.CharField(blank=True, max_length=10, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="phone.phone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientLegalPerson",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("ICO", models.CharField(blank=True, max_length=10, null=True)),
                ("DIC", models.CharField(blank=True, max_length=10, null=True)),
                ("VAT_payer", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="phone.phone",
                    ),
                ),
            ],
        ),
    ]
