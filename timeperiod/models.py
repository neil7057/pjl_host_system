from django.db import models
from django.core.exceptions import ValidationError


class Timeperiod(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False,)
    date_from = models.DateField(blank=False, null=False)
    date_to = models.DateField(blank=False, null=False)

    def clean(self):
        if self.date_from >= self.date_to:
            raise ValidationError({
                'date_from': 'Start date must be before end date',
                'date_to': 'by at least one day',
            })

    def __str__(self):
        return self.title
