# Generated by Django 4.0.4 on 2022-05-23 05:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 8, 4, 42, 989297)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 8, 4, 42, 987302)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 8, 4, 42, 984311)),
        ),
    ]
