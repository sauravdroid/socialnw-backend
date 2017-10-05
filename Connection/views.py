from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import *
from django.contrib.auth.models import User
from rest_framework import status
from django.core.exceptions import ValidationError
from .serializer import RequestSerializer, FollowerSerializer, AllFollowerSerializer, AllFollowingSerializer
from UserAuthentication.serializer import UserSerializer
from Post.serializer import PostSerializer


class HandleRequest(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            requested_user = User.objects.get(username=request.data['username'])
            # if check_reverse_invitation(request.user, requested_user):
            #     print("User Invitation Exists")
            #     return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
            # else:
            invitationRequest = Request(user=request.user, requested_user=requested_user)
            invitationRequest.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        except:
            # request.delete()
            return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)


class GetRequests(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        requestList = Request.objects.filter(requested_user=request.user, request_status=False)
        serializer = RequestSerializer(requestList, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class HandleInvitation(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        try:
            follower_user = User.objects.get(username=request.data['username'])
            invitationRequest = Request.objects.get(user=follower_user, requested_user=request.user)
            if request.data['approval_status'] == 'accept':
                follower = Follower(user=request.user, follower=follower_user)
                following = Following(user=follower_user, following_user=request.user)
                invitationRequest.request_status = True
                follower.save()
                following.save()
                invitationRequest.save()
            else:
                invitationRequest.delete()
            return Response({'success': True, 'request': request.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)


class CheckRequested(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        user = User.objects.get(username=request.data['username'])
        try:
            request = Request.objects.get(user=user, requested_user=request.user)
            return Response({'success': False, 'request_status': request.request_status}, status=status.HTTP_200_OK)
        except Request.DoesNotExist:
            return Response({'success': True}, status=status.HTTP_200_OK)


class CheckSent(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        user = User.objects.get(username=request.data['username'])
        try:
            request = Request.objects.get(user=request.user, requested_user=user)
            return Response({'success': False, 'request_status': request.request_status}, status=status.HTTP_200_OK)
        except Request.DoesNotExist:
            return Response({'success': True}, status=status.HTTP_200_OK)


class CheckFollower(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        follower_user = User.objects.get(username=request.data['username'])
        isFollower = False
        isFollowing = False
        sentRequest = False
        hasRequested = False
        try:
            follower = Follower.objects.get(user=request.user, follower=follower_user)
            isFollower = True
        except Follower.DoesNotExist:
            isFollower = False

        try:
            following = Follower.objects.get(user=follower_user, follower=request.user)
            isFollowing = True
        except Follower.DoesNotExist:
            isFollowing = False

        try:
            requestInvitation = Request.objects.get(user=request.user, requested_user=follower_user)
            if requestInvitation.request_status == False:
                sentRequest = True
            else:
                sentRequest = False
        except Request.DoesNotExist:
            sentRequest = False

        try:
            hasRequestedInvitation = Request.objects.get(requested_user=request.user, user=follower_user)
            if hasRequestedInvitation.request_status == False:
                hasRequested = True
            else:
                hasRequested = False
        except Request.DoesNotExist:
            hasRequested = False

        return Response({"isFollower": isFollower, "isFollowing": isFollowing, "sentRequest": sentRequest,
                         "hasRequested": hasRequested},
                        status=status.HTTP_200_OK)


class AllFollowers(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        followings = request.user.followings.all()
        postsResult = []
        for post in request.user.posts.all():
            postsResult.append(post)
        for following in followings:
            for post in following.following_user.posts.all():
                postsResult.append(post)
        print(postsResult)
        serializer = PostSerializer(postsResult, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllPostsByLoggedInUser(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        posts = request.user.posts.all()
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserFollowers(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        followers = Follower.objects.filter(user=request.user)
        allFollowers = []
        for follower in followers:
            followerCount = follower.follower.followers.count()
            followingCount = follower.follower.followings.count()
            allFollowers.append({
                'followerCount': followerCount,
                'followingCount': followingCount,
            })
        serializer = AllFollowerSerializer(followers, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserFollowing(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        followings = Following.objects.filter(user=request.user)
        serializer = AllFollowingSerializer(followings, many=True, context={"request": request})
        return Response(serializer.data,status=status.HTTP_200_OK)


def check_reverse_invitation(user, requested_user):
    try:
        invitation = Request.objects.get(user=requested_user, requested_user=user)
        print("User Request Exist")
        return True
    except Request.DoesNotExist:
        print("User Request Does Not Exist")
        return False
