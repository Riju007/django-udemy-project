"""Serializer for the app movies."""
from rest_framework import serializers

from movies.models import MovieData


class MovieSerializer(serializers.ModelSerializer):
    """Serialize the MovieData model."""

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        """Meta class for the class."""

        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
