# Generated by Django 4.2.9 on 2024-02-26 21:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0041_visibleonsite_reobjectvisibleonsite"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reobjectvisibleonsite",
            old_name="page",
            new_name="visible_on_site",
        ),
    ]
