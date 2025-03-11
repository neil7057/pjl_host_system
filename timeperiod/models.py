from django.db import models


class Timeperiod(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False,)
    date_from = models.DateField(blank=False, null=False)
    date_to = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title
