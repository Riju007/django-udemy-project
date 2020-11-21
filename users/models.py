"""Models for the users app."""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Created profile model for users.

    Every user will have profile. If the user is deleted the profile will also
    be deleted.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        default='profilepic.jpg',
        upload_to='profile_pictures'
    )
    location = models.CharField(
        max_length=100
    )

    def __str__(self):
        """Represent the profile object as a string."""
        return self.user.username
