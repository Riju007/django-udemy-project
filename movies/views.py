"""Views for the app movies."""
from rest_framework import viewsets

from movies.serializers import MovieSerializer
from movies.models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    """Viewset for the movie data."""

    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    """API endpoint view for action movies."""

    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    """API endpoint for the comedy movies."""

    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer
