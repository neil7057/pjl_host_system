from django.db import models


class Organisation(models.Model):
    orgname = models.CharField(max_length=254)
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40, null=True, blank=True)
    town = models.CharField(max_length=40)
    postcode = models.CharField(max_length=8)
    county = models.CharField(max_length=20, default="East Sussex")
    telephone = models.CharField(max_length=14, null=True)
    contact_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.orgname
