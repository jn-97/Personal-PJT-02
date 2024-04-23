from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class PostList(APIView):

  def get(self, request):

    model = Post.objects.all()
    serializer = PostSerializer(model, many=True)
    return Response(serializer.data)