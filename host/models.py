from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


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
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.hostname
