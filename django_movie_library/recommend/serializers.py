from django_movie_library.movie.models import Movie
from django_movie_library.movie.serializers import MovieSerializer


class MovieRecommendation(MovieSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre', 'rating', 'rating_count']
        depth = 1