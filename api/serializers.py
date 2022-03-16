from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Movie, Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre')


class UserAddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'rating', 'notes', 'added_at', 'genre', 'added_by']


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

