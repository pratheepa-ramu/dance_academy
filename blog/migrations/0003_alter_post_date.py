# Generated by Django 4.2.13 on 2024-06-12 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 12, 13, 17, 51, 967581)
            ),
        ),
    ]
