from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=200)

    # Foreign key representing the user this list belongs to.
    owner = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

class Item(models.Model):
    title = models.CharField(max_length=200)
    archived = models.BooleanField(default=False)

    # Foreign key representing the list that this item belongs to.
    parent_list = models.ForeignKey('List', related_name='items', on_delete=models.CASCADE)