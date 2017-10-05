from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializer import UserProfileSerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import Http404
from UserAuthentication.serializer import UserSerializer
from UserProfile.models import Profile


class UpdateUserProfile(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, user):
        try:
            user_profile = Profile.objects.get(user=user)
            return user_profile
        except Profile.DoesNotExist:
            return Http404

    def put(self, request, format=None):
        try:  # Updating User
            user = request.user
            print("Updating User Data")
            user_profile = self.get_object(user=user)
            serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=user)

                if request.data.get('first_name', None) is not None:
                    request.user.first_name = request.data.get('first_name')

                if request.data.get('last_name', None) is not None:
                    request.user.last_name = request.data.get('last_name')

                request.user.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        except:  # Creating new User
            serializer = UserProfileSerializer(data=request.data, partial=True)
            print("Creating User Data")
            if serializer.is_valid():
                serializer.save(user=request.user)
                request.user.first_name = request.data.get('first_name')
                request.user.last_name = request.data.get('last_name')
                request.user.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    authentication_classes = (TokenAuthentication,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfile(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchUser(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        username = request.data.get('username',"")
        users = User.objects.filter(username__startswith=username)
        serializer = UserSerializer(users, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class CheckNewUser(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        response_object = {'new_user': False}
        try:
            request.user.user_profile
        except ObjectDoesNotExist:
            response_object = {'new_user': True}
        return Response(response_object, status=status.HTTP_200_OK)
