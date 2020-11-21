"""URLs for the app users."""
from django.urls import path

from users.views import register, user_profile

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register_user'),
    path('profile/', user_profile, name='profile'),
]
