# Generated by Django 4.2.9 on 2024-09-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0062_reobject_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reobject",
            name="id",
            field=models.TextField(
                help_text="ID объекта",
                max_length=255,
                unique=True,
                verbose_name="ID объекта",
            ),
        ),
    ]
