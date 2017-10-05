from django.conf.urls import url
from . import views

app_name = 'user_authentication'
urlpatterns = [
    url(r'^login/$',views.UserLogin.as_view(),name='login'),
    url(r'^register/$',views.UserRegistration.as_view(),name='register'),
    url(r'^update/$',views.UserUpdate.as_view()),
    url(r'^simple/$',views.SimpleView.as_view()),
]