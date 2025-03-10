from django.db import models


class Teamlead(models.Model):
    first_name = models.CharField(max_length=40, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=60, blank=False, null=True)
    mobile = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.first_name
