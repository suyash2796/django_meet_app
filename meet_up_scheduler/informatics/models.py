from django.db import models
from datetime import time

# Create your models here.

class Seminar(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(default =time(9))
    duration = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.title} at {self.time} on {self.date}"
