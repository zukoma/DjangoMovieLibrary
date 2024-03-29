from django.contrib.auth.models import User
from rest_framework import serializers
from django_movie_library.movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'notes', 'genre', 'added_at', 'rating', 'rating_count']

    def get_rating(self, obj):
        return obj.get_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class UserAddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = User(**validate_data)
        user.set_password(password)
        user.save()
        return user


class RecommendationsResponseSerializer(MovieSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre', 'rating', 'rating_count']
        depth = 1