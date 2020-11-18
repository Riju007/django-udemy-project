"""URLs for the food app."""
from django.urls import path

from food.views import (
    list_item, view_item, create_item, update_item, delete_item, home
)


# namespacing
app_name = 'food'

urlpatterns = [
    path("", home, name='home'),
    path("item-list/", list_item, name='food_list_view'),
    path('item-detail/<int:item_id>/', view_item, name='item_detail_view'),
    # add items
    path('item-create/', create_item, name='item_create_view'),
    # edit item
    path('item-update/<int:id>/', update_item, name='item_update_view'),
    # delete
    path('item-delete/<int:id>/', delete_item, name='delete_item_view'),
]
