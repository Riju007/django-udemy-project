from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://th.bing.com/th/id/OIP.nLDShz9SB5YleA3GH5fJJAHaHa?pid=Api&rs=1")

    def __str__(self):
        return self.item_name
