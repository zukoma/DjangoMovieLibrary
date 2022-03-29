from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_movie_library.recommend.serializers import MovieRecommendation
from django_movie_library.movie.models import Movie, Genre
import random


@api_view(['POST'])
def get_recommendation(request):
    if request.data['genre']:
        genre_name = request.data['genre']
        genre = Genre.objects.filter(name=genre_name).first()

        if genre:
            genre_id = genre.id
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        similar_movies_by_genre = list(Movie.objects.filter(genre=genre_id))
        recommendation = random.choice(similar_movies_by_genre)
        serializer = MovieRecommendation(recommendation)
        return Response(serializer.data)
    elif request.data['rating']:
        rating = request.data['rating']
        recommendation = Movie.objects.filter(ratings__user_id__gte=rating)
        serializer = MovieRecommendation(recommendation)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
