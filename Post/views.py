from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializer import PostSerializer, PostLikeSerializer
from rest_framework import status
from .models import Post, PostLike
from django.http import Http404


class CreatePost(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, context={"request": request})
        print(post.cover_pic.url)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikePost(APIView):
    authentication_classes = (TokenAuthentication,)

    def get_object(self, pk, user):
        try:
            post = Post.objects.get(pk=pk)
            return PostLike.objects.get(post=post, user=user)
        except PostLike.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        try:
            post = Post.objects.get(pk=request.data['post_id'])
            postLikeInstance = self.get_object(request.data['post_id'],request.user)
            serializer = PostLikeSerializer(postLikeInstance, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, post=post, like_status=not postLikeInstance.like_status)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            serializer = PostLikeSerializer(data=request.data)
            post = Post.objects.get(pk=request.data['post_id'])
            if serializer.is_valid():
                serializer.save(user=request.user, post=post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
