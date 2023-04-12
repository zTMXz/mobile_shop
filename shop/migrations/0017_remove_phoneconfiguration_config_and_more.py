# Generated by Django 4.1.7 on 2023-04-11 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0016_remove_phoneconfigurations_phone_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="phoneconfiguration", name="config",),
        migrations.AddField(
            model_name="phoneconfiguration",
            name="config_slug",
            field=models.CharField(default="", max_length=250),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 18, 42, 14, 845108)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 18, 42, 14, 845108)
            ),
        ),
    ]
