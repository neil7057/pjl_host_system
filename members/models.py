from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator)


class Members(models.Model):
    first_name = models.CharField(max_length=254, blank=False, null=True)
    last_name = models.CharField(max_length=254, blank=False, null=True)
    email = models.EmailField(max_length=254, blank=False, null=True)
    is_adult = models.BooleanField(default=True, null=True, blank=False)
    is_child = models.BooleanField(default=False, null=True, blank=False)
    child_age = models.IntegerField(
                                    validators=[MaxValueValidator(17),
                                                MinValueValidator(1)])
    valid_dbs = models.BooleanField(default=True, null=True, blank=False)
    dbs_date = models.DateField()

    def __str__(self):
        return self.name
