from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import *
from Post.models import Post
from rest_framework import status
from .serializer import CommentSerializer


class AddComment(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        post = Post.objects.get(pk=request.data['post_id'])
        serializer = CommentSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(owner=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
