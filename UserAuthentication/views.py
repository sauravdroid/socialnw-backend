from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token


class UserRegistration(APIView):
    def post(self, request, format=None):
        password = request.data.get('password')
        numberCount = 0
        containsSpecial = False
        if set('[~!@#$%^&*()_+{}":;\']+$').intersection(password):
            containsSpecial = True
        for char in password:
            try:
                int(char)
                numberCount += 1
            except ValueError:
                pass
        if numberCount > 0 and containsSpecial:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid Password,password should be alphanumeric and contain one special character",status=status.HTTP_400_BAD_REQUEST)



class UserLogin(APIView):
    authentication_classes = (BasicAuthentication,)

    def post(self, request, format=None):
        token = Token.objects.get(user=request.user)
        return Response({'user_token': 'Token ' + token.key, 'username': token.user.username})


class SimpleView(APIView):
    def get(self, request):
        return Response({'Data': 'Hello World'})


class UserUpdate(APIView):
    authentication_classes = (TokenAuthentication,)

    def put(self, request, format=None):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
