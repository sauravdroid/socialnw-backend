from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('UserAuthentication.urls')),
    url(r'^update/', include('UserProfile.urls')),
    url(r'^post/', include('Post.urls')),
    url(r'^connect/', include('Connection.urls')),
    url(r'^comment/', include('Comment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)