# Generated by Django 5.0.1 on 2024-01-13 21:57

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desks_app', '0003_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2024, 1, 13, 21, 57, 5, 502611))]),
        ),
    ]
