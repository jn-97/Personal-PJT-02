from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class PostList(APIView):

  def get(self, request):

    model = Post.objects.all()
    serializer = PostSerializer(model, many=True)
    return Response(serializer.data)
  
  def post(self, request):

    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class PostDetail(APIView):

  def get(self, request, id):

    model = Post.objects.get(id=id)
    serializer = PostSerializer(model)
    return Response(serializer.data)
  
  def put(self, request, id):

    model = Post.objects.get(id=id)
    serializer = PostSerializer(model, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id):

    model = Post.objects.get(id=id)
    model.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)