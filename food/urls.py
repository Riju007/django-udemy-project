"""URLs for the food app."""
from django.urls import path

from food.views import (
    update_item, delete_item, FoodListView, FoodDetailView, FoodCreateView
)

# namespacing
app_name = 'food'

urlpatterns = [
    path("item-list/", FoodListView.as_view(), name='food_list_view'),
    path(
        'item-detail/<int:pk>/',
        FoodDetailView.as_view(), name='item_detail_view'),
    # add items
    path('item-create/', FoodCreateView.as_view(), name='item_create_view'),
    # edit item
    path('item-update/<int:id>/', update_item, name='item_update_view'),
    # delete
    path('item-delete/<int:id>/', delete_item, name='delete_item_view'),
]
