from django.db import models

# Create your models here.

from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200,
                            default="")
    date = models.DateField(default="2019-01-01")
    location = models.CharField(max_length=200,
                                default="default location")
    description = models.TextField(default="default description")

    def __str__(self):
        return self.name
