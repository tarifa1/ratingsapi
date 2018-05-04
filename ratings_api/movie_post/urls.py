from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.MoviesList.as_view()),
    url(r'(\d+)/$', views.MoviesDetail.as_view()),
]