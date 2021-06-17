from django.db import models

# Create your models here.
class Notes(models.Model):
    note = models.CharField(max_length=200)