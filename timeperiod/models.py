from django.db import models
from pupil.models import Pupil


class Timeperiod(models.Model):
    date_from = models.DateField(blank=False, null=False)
    date_to = models.DateField(blank=False, null=False)
    pupil = models.ForeignKey(
        Pupil, on_delete=models.SET_NULL, related_name="time",
        null=True, blank=True)

    def __str__(self):
        return self.name
