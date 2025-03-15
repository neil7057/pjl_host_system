from django.db import models
from organisation.models import Organisation


class Teamlead(models.Model):
    first_name = models.CharField(max_length=40, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=60, blank=False, null=True)
    mobile = models.CharField(max_length=12, blank=False, null=False)
    org = models.ForeignKey(
        Organisation, on_delete=models.SET_NULL, related_name="org",
        null=True, blank=False)

    def __str__(self):
        return self.first_name
