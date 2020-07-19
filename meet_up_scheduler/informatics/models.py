from django.db import models
from datetime import time

# Create your models here.

class City(models.Model):
    pin_code = models.IntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return f"seminar in {self.city} at {self.address}"

class Seminar(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(default =time(9))
    duration = models.IntegerField(default = 1)
    city = models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.time} on {self.date}"

