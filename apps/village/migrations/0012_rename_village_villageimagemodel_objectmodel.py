# Generated by Django 4.2.9 on 2024-03-05 22:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps_village", "0011_alter_villageemployee_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="villageimagemodel",
            old_name="village",
            new_name="objectModel",
        ),
    ]