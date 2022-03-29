from django_movie_library.movie.models import Movie
from django_movie_library.movie.serializers import MovieSerializer


class RecommendMovieSerializer(MovieSerializer):
    # TODO better name would be MovieRecommendation
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre', 'rating', 'rating_count']
        depth = 1