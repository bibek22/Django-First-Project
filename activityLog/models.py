from django.db import models


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=10)
    done = False
    description = models.TextField()
    remarks = models.TextField()

    def __str__(self):
        return self.name
