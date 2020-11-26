"""Views for the app movies."""
from django.shortcuts import render
from rest_framework import viewsets

from movies.serializers import MovieSerializer
from movies.models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    """Viewset for the movie data."""

    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
