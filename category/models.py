from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, blank=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
