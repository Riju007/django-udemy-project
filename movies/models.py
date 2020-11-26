"""Models for the app movies."""
# 3rd party imports
from django.db import models


class MovieData(models.Model):
    """Define a model to represent movie data."""

    name = models.CharField('movie name', max_length=200,)
    duration = models.FloatField('movie duration')
    rating = models.FloatField('movie rating')

    def __str__(self):
        """Define object representation of the model."""
        return self.name
