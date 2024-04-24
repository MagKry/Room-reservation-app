from _datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_size = models.IntegerField(default=0)
    projector = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room_name}, {self.room_size}, {self.projector}"


class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ("date", "room_id",)
