from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()
    