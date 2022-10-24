# Generated by Django 4.1.1 on 2022-10-23 19:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
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
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("price", models.PositiveIntegerField()),
                ("description", models.TextField(null=True)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="pictures"),
                ),
            ],
            options={
                "verbose_name": "Обьявление",
                "verbose_name_plural": "Обьявления",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        max_length=60, unique=True, verbose_name="Название категории"
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(5)],
                        verbose_name="Слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Selection",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("items", models.ManyToManyField(to="ads.ad")),
            ],
            options={
                "verbose_name": "Подборка объявлений",
                "verbose_name_plural": "Подборки объявлений",
            },
        ),
    ]
