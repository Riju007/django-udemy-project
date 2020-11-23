"""Models for the food app."""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    """Define a model for food items."""

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://th.bing.com/th/id/OIP.nLDShz9SB5YleA3GH5fJJAHaHa?pid=Api&rs=1")

    def __str__(self):
        """Display the food object."""
        return self.item_name

    def get_absolute_url(self):
        """View for the object url."""
        return reverse('food:item_detail_view', kwargs={'pk': self.pk})
