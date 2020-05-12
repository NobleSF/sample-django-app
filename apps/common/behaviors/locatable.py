from django.db import models


class Locatable(models.Model):

    address = models.ForeignKey('common.Address', null=True, blank=True, on_delete=models.SET_NULL)

    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True
