# Generated by Django 4.1.7 on 2023-04-14 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0032_phonedetails_camera_en_phonedetails_camera_ru_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="description_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="ph_color_name_en",
            field=models.CharField(default="", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="ph_color_name_ru",
            field=models.CharField(default="", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 14, 9, 58, 13, 505257)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 14, 9, 58, 13, 505257)
            ),
        ),
    ]
