# Generated by Django 4.2.13 on 2024-06-12 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 12, 11, 44, 39, 43319)
            ),
        ),
    ]
