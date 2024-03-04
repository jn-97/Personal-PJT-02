from django.db import models
from django.contrib.auth.models import AbstractUser
from community.models import Post

# Create your models here.
class User(AbstractUser):
  bookmarks = models.ManyToManyField(Post, related_name='bookmarked_by')
