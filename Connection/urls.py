from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^request/$',views.HandleRequest.as_view()),
    url(r'^request/handle/$',views.HandleInvitation.as_view()),
    url(r'^request/requested/$',views.CheckRequested.as_view()),
    url(r'^request/sent/$',views.CheckSent.as_view()),
    url(r'^request/all/$',views.GetRequests.as_view()),
    url(r'^request/check/$',views.CheckFollower.as_view()),
    url(r'^request/followers/$',views.AllFollowers.as_view()),
    url(r'^request/mine/$',views.AllPostsByLoggedInUser.as_view()),
    url(r'^request/allfollowers/$',views.UserFollowers.as_view()),
    url(r'^request/allfollowings/$',views.UserFollowing.as_view()),
]