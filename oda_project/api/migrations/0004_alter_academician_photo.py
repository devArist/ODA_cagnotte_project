# Generated by Django 3.2.12 on 2022-02-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_academician_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academician",
            name="photo",
            field=models.FileField(blank=True, upload_to="image_academician"),
        ),
    ]
