from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator)


class Host(models.Model):
    hostname = models.CharField(max_length=254)
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40, null=True, blank=True)
    town = models.CharField(max_length=40)
    postcode = models.CharField(max_length=8)
    county = models.CharField(max_length=20, default="East Sussex")
    telephone = models.CharField(max_length=14, null=True)
    max_occupants = models.IntegerField(
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(8)],)
    gas_safety = models.BooleanField(default=False, blank=True)
    gas_safety_date = models.DateField()

    def __str__(self):
        return self.hostname
