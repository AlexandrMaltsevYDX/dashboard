# Generated by Django 4.2.9 on 2024-02-07 14:07

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "text",
                    mdeditor.fields.MDTextField(
                        blank=True, null=True, verbose_name="Текст с форматированием"
                    ),
                ),
                (
                    "author_name",
                    models.CharField(
                        blank=True,
                        help_text="например: Андреева Любовь, Кох И.С.",
                        max_length=1000,
                        null=True,
                        verbose_name="Имя автора полностью",
                    ),
                ),
                (
                    "link_to_src",
                    models.CharField(
                        blank=True,
                        help_text="Скопируйте ссылку отзыва и поместите в это поле",
                        max_length=1000,
                        null=True,
                        verbose_name="Ccылка на источник",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.CreateModel(
            name="ReviewImageModel",
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
                ("image", models.FileField(upload_to="reviews/")),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review",
                        to="apps_reviews.review",
                    ),
                ),
            ],
            options={
                "verbose_name": "Скрин или фото к ревью",
                "verbose_name_plural": "Скрин или фото к ревью",
            },
        ),
    ]
