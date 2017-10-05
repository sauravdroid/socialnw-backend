from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UpdateUserProfile.as_view()),
    url(r'^check$', views.CheckNewUser.as_view()),
    url(r'^(?P<username>[\w.@\-]+)/$', views.UserDetail.as_view()),
    url(r'^profile$', views.UserProfile.as_view()),
    url(r'^search', views.SearchUser.as_view()),

]
