# Generated by Django 5.0.1 on 2024-01-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desks_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='projector',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='room_size',
            field=models.IntegerField(default=0),
        ),
    ]
