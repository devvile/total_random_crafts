# Generated by Django 3.0.6 on 2020-05-30 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 13, 31, 0, 220284, tzinfo=utc)),
        ),
    ]
