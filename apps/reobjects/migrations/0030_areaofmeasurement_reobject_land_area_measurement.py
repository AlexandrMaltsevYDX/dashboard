# Generated by Django 4.2.9 on 2024-02-09 19:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0029_driveways_reobject_driveways"),
    ]

    operations = [
        migrations.CreateModel(
            name="AreaOfMeasurement",
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
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Название единицы измерения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Единица измерения площади",
                "verbose_name_plural": "Единицы измерения площади",
            },
        ),
        migrations.AddField(
            model_name="reobject",
            name="land_area_measurement",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите из списка, или создайте новое '+'",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="apps_reobjects.areaofmeasurement",
                verbose_name="Единицы измерения площади участка",
            ),
        ),
    ]
