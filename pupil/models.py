from django.db import models
from organisation.models import Organisation
from teamlead.models import Teamlead


class Pupil(models.Model):
    first_name = models.CharField(max_length=40, blank=False, null=True)
    preferred_name = models.CharField(max_length=40, blank=False, null=True)
    last_name = models.CharField(max_length=40, blank=False, null=True)
    nationality = models.CharField(max_length=40, blank=False, null=True)
    gender = models.BooleanField(blank=False, null=True)
    dob = models.DateField(blank=False, null=True)
    org = models.ForeignKey(
        Organisation, on_delete=models.SET_NULL, related_name="organisation",
        null=True, blank=True)
    team = models.ForeignKey(
        Teamlead, on_delete=models.SET_NULL, related_name="teamlead",
        null=True, blank=True)

    def __str__(self):
        return self.first_name
