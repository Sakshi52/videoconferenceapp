from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
