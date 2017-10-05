from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.CreatePost.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CreatePost.as_view()),
    url(r'^like/$', views.LikePost.as_view()),
]
