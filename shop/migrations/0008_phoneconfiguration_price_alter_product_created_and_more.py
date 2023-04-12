# Generated by Django 4.1.7 on 2023-04-11 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_product_camera_product_os_product_screen_size_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="phoneconfiguration",
            name="price",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 14, 6, 59, 730678)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 14, 6, 59, 730678)
            ),
        ),
    ]
