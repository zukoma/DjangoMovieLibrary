from rest_framework import serializers
from django_movie_library.ratings.models import Ratings


class RatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = ['user', 'movie', 'rating']

    def validate(self, data):
        if Ratings.objects.filter(movie=data['movie'], user=data['user']).exists():
            raise serializers.ValidationError("User has already rated this movie")
        return data
