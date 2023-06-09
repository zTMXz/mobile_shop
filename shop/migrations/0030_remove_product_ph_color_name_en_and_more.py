# Generated by Django 4.1.7 on 2023-04-14 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0029_product_ph_color_name_en_product_ph_color_name_ru_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="ph_color_name_en",),
        migrations.RemoveField(model_name="product", name="ph_color_name_ru",),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 14, 9, 47, 16, 249447)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 14, 9, 47, 16, 249447)
            ),
        ),
    ]
