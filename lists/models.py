from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # Link this profile model to the user model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Signal to sync profile models to user models.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # If a new user model was created, make a new profile.
        Profile.objects.create(user=instance)
    else:
        # If the user model exists, save its profile instance.
        instance.profile.save()


class List(models.Model):
    name = models.CharField(max_length=200)

    # Foreign key representing the user this list belongs to.
    owner = models.ForeignKey('Profile', related_name='lists', on_delete=models.CASCADE)


class Item(models.Model):
    title = models.CharField(max_length=200)
    archived = models.BooleanField(default=False)

    # Foreign key representing the list that this item belongs to.
    parent_list = models.ForeignKey('List', related_name='items', on_delete=models.CASCADE)