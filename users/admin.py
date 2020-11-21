"""Register models in the admin page."""
from django.contrib import admin

from users.models import Profile


admin.site.register(Profile)
