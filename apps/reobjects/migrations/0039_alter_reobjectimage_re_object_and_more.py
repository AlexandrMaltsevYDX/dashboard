# Generated by Django 4.2.9 on 2024-02-22 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0038_approveusage_reobject_approve_usage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reobjectimage",
            name="re_object",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photo_images",
                to="apps_reobjects.reobject",
            ),
        ),
        migrations.AlterField(
            model_name="reobjectplanmodel",
            name="re_object",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plans_images",
                to="apps_reobjects.reobject",
            ),
        ),
    ]
