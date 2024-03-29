# Generated by Django 4.2.9 on 2024-01-30 20:20

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0005_reobjectmodel_and_more"),
        ("apps_blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
            ],
            options={
                "verbose_name": "Тэг поста",
                "verbose_name_plural": "Тэги поста",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="apps_users.employeeprofilemodel",
                verbose_name="Автор поста",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=mdeditor.fields.MDTextField(
                blank=True, null=True, verbose_name="Текст с форматированием"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="name",
            field=models.TextField(
                blank=True,
                help_text="Введите текст",
                max_length=255,
                verbose_name="Название поста",
            ),
        ),
        migrations.CreateModel(
            name="PostTagsModel",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_images",
                        to="apps_blog.post",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_tags",
                        to="apps_blog.tag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Relations posts mtm tags",
                "verbose_name_plural": "Relations posts mtm tags",
            },
        ),
        migrations.CreateModel(
            name="PostImageModel",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("image", models.FileField(upload_to="avatars/")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="postimages",
                        to="apps_blog.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото поста",
                "verbose_name_plural": "Фото поста",
            },
        ),
    ]
