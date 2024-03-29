# Generated by Django 4.2.9 on 2024-02-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0011_employeeprofilemodel_job_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employeeprofilemodel",
            name="position",
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="job_title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="apps_users.jobtitle",
                verbose_name="Должность",
            ),
        ),
    ]
