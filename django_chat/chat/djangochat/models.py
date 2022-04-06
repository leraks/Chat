from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)


class Dict_user(models.Model):
    container = models.ForeignKey(Room, on_delete=models.CASCADE)
    key = models.CharField(max_length=240, db_index=True)
    value = models.CharField(max_length=240, db_index=True)

class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=10000)
