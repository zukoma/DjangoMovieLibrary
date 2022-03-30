from django_movie_library.movie.models import Movie
from django_movie_library.movie.serializers import MovieSerializer
from rest_framework import serializers
from .models import Recommendations


class RecommendationsResponseSerializer(MovieSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre', 'rating', 'rating_count']
        depth = 1


class ReommendationsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ['user', 'recommended_movie', 'recommended_at']
