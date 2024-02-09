# Generated by Django 4.2.9 on 2024-02-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0026_reobject_yandex_map_link_reobject_you_tube_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="reobject",
            name="ceiling_height",
            field=models.FloatField(
                blank=True,
                help_text="Ведите цифры в метрах например '3.2'",
                null=True,
                verbose_name="Высота потолков",
            ),
        ),
        migrations.AddField(
            model_name="reobject",
            name="date_sale",
            field=models.DateField(
                blank=True,
                help_text="введите дату",
                null=True,
                verbose_name="Дата продажи",
            ),
        ),
        migrations.AddField(
            model_name="reobject",
            name="wc",
            field=models.TextField(
                blank=True,
                help_text="Введите текст",
                max_length=255,
                null=True,
                verbose_name="Санузел",
            ),
        ),
    ]