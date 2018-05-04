from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url('admin/', admin.site.urls),
    url('', admin.site.urls),
    url('movies/', include('movie_post.urls')),
    url('api/', include('movie_post.urls')),
]