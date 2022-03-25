from rest_framework import serializers
from django_movie_library.ratings.models import Ratings


class RatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = ['user', 'movie', 'rating']
