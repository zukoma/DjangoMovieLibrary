from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_movie_library.movie.serializers import MovieSerializer
from django_movie_library.recommend.serializers import RecommendMovieSerializer
from django_movie_library.movie.models import Movie, Genre
import random


@api_view(['POST'])
def get_recommendation(request):
    if request.method == 'POST':
        genre_name = request.data['genre']
        genre_id = Genre.objects.filter(name=genre_name)[0].id

        similar_movies_by_genre = list(Movie.objects.filter(genre=genre_id))
        recommendation = random.choice(similar_movies_by_genre)

        serializer = RecommendMovieSerializer(recommendation)

        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
