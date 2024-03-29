# Generated by Django 4.2.9 on 2024-02-05 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0010_coordinates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coordinates",
            name="ydx_latitude",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Широта(Яндекс)"
            ),
        ),
        migrations.AlterField(
            model_name="coordinates",
            name="ydx_longitude",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Долгота(Яндекс)"
            ),
        ),
        migrations.AlterField(
            model_name="reobjectengineeringservices",
            name="engineering_service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="engineering_services",
                to="apps_reobjects.engineeringservices",
                verbose_name="Коммуникации",
            ),
        ),
    ]
