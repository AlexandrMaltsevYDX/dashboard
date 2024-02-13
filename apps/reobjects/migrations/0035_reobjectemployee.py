# Generated by Django 4.2.9 on 2024-02-13 19:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0012_remove_employeeprofilemodel_position_and_more"),
        ("apps_reobjects", "0034_salesmethod_reobject_sales_method"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReObjectEmployee",
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
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agents",
                        to="apps_users.employeeprofilemodel",
                    ),
                ),
                (
                    "re_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reobjectemployees",
                        to="apps_reobjects.reobject",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
