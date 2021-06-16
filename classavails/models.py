from django.db import models

# Create your models here.

class Greeting(models.Model):
    CRN = models.PositiveIntegerField()
    department = models.CharField(max_length=200)
    courseNumber = models.PositiveIntegerField()
    