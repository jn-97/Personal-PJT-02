from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

  class Meta:

    model = Post
    fields = ['writer', 'category', 'title', 'contents']