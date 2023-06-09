# Generated by Django 4.1.7 on 2023-04-11 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_remove_product_show_alter_product_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="phoneconfiguration",
            name="config",
            field=models.ManyToManyField(to="shop.product"),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 15, 26, 10, 920150)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 15, 26, 10, 920150)
            ),
        ),
    ]
