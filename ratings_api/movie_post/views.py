from rest_framework import generics

from . import models
from . import serializers


class MoviesList(generics.ListAPIView):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializer


class MoviesDetail(generics.RetrieveAPIView):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializer