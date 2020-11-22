"""Signals for the app users."""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    """Build the profile of the user when the user registers."""
    if created:
        print('User is created')
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Save the profile into the db."""
    print('Save profile called')
    instance.profile.save()
