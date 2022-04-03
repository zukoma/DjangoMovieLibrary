from django_movie_library.movie.models import Movie
from django_movie_library.movie.serializers import MovieSerializer
from rest_framework import serializers
from .models import Recommendations


class ReommendationsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ['user', 'recommended_movie', 'recommended_at']
        depth = 0


class ViewReadSerializer(ReommendationsModelSerializer):
    class Meta:
        model = Recommendations
        fields = ['user', 'recommended_movie', 'recommended_at']
        depth = 1

