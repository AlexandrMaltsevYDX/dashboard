# Generated by Django 4.2.9 on 2024-09-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0064_alter_reobject_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reobject",
            name="id",
            field=models.TextField(
                help_text="Максимум 10 символов",
                max_length=10,
                unique=True,
                verbose_name="ID объекта",
            ),
        ),
    ]
