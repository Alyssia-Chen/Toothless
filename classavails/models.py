from django.db import models
from django.views.generic.detail import SingleObjectTemplateResponseMixin

# Create your models here.

class ClassAvails(models.Model):
    CRN = models.PositiveIntegerField()
    course = models.CharField(max_length=10, default='ABC 000')
    section = models.IntegerField(default = -1)
    title = models.CharField(max_length=100, default = 'XXXXXX')
    credits = models.CharField(max_length=25, default='-1')
    instructor = models.CharField(max_length=50, default = 'XXXXXXXXX')
    curEnrolled = models.IntegerField(default = -1)
    seatsAvail = models.IntegerField(default = -1)
    curWaitlisted = models.IntegerField(default = -1)
    waitlistAvailable = models.IntegerField(default = -1)
    days = models.CharField(max_length=10, default = -1)
    time = models.CharField(max_length=100, default = 'XX-XX')
    location = models.CharField(max_length=50, default = 'XXX')
    dates = models.CharField(max_length=50, default = 'XXX')

    def __str__(self):
        # LATER Add a tostring representation of CRN?
        return self.title
