# Generated by Django 4.1.7 on 2023-04-13 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0026_product_details_alter_product_created_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="phonecolors",
            options={"verbose_name": "Цвет", "verbose_name_plural": "Цвета телефонов"},
        ),
        migrations.AlterModelOptions(
            name="phoneconfiguration",
            options={
                "verbose_name": "Конфигурация",
                "verbose_name_plural": "Конфигурации телефонов",
            },
        ),
        migrations.AlterModelOptions(
            name="phonedetails",
            options={
                "ordering": ("model",),
                "verbose_name": "Детали телефона",
                "verbose_name_plural": "Детали телефонов",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "Телефон",
                "verbose_name_plural": "Телефоны",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 13, 23, 27, 58, 322064)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 13, 23, 27, 58, 322064)
            ),
        ),
    ]
