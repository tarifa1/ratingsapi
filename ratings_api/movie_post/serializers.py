from rest_framework import serializers
from . import models


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title', 'rating', 'created_at', 'updated_at',)
        model = models.Movies