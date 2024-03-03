# Generated by Django 4.2.9 on 2024-02-26 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0013_employeeprofilemodel_location"),
        ("apps_reobjects", "0039_alter_reobjectimage_re_object_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reobjectemployee",
            options={"verbose_name": "Агенты", "verbose_name_plural": "Агенты"},
        ),
        migrations.AlterModelOptions(
            name="reobjectengineeringservices",
            options={
                "verbose_name": "Инженерные коммуникации",
                "verbose_name_plural": "Инженерные коммуникации",
            },
        ),
        migrations.RemoveField(
            model_name="reobject",
            name="visible_on_site",
        ),
        migrations.AlterField(
            model_name="reobjectemployee",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agents",
                to="apps_users.employeeprofilemodel",
                verbose_name="Агент",
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