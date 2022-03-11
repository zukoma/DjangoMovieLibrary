from rest_framework import serializers
from api.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'rating', 'notes', 'added_at']
