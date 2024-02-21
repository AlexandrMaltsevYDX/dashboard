# Generated by Django 4.2.9 on 2024-02-13 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0010_jobtitle"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeeprofilemodel",
            name="job_title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="apps_users.jobtitle",
            ),
        ),
    ]