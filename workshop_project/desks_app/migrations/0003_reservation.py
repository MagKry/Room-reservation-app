# Generated by Django 5.0.1 on 2024-01-13 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desks_app', '0002_room_projector_room_room_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('date', models.DateField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desks_app.room')),
            ],
            options={
                'unique_together': {('date', 'id')},
            },
        ),
    ]