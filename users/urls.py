"""URLs for the app users."""
from django.urls import path

from users.views import register, user_profile, UserLoginView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register_user'),
    path('profile/', user_profile, name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
