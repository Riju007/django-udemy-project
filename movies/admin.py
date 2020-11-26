"""Admin file for the app movies."""
from django.contrib import admin

from movies.models import MovieData

admin.site.register(MovieData)
