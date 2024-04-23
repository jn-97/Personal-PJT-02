from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

  writer = serializers.CharField(required=False)
  title = serializers.CharField(required=False)
  contents = serializers.CharField(required=False)

  class Meta:

    model = Post
    fields = '__all__'