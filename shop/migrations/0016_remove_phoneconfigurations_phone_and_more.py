# Generated by Django 4.1.7 on 2023-04-11 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_alter_phone_main_configuration_alter_product_created_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="phoneconfigurations", name="phone",),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 18, 3, 59, 194190)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 18, 3, 59, 194190)
            ),
        ),
        migrations.DeleteModel(name="Phone",),
        migrations.DeleteModel(name="PhoneConfigurations",),
    ]
