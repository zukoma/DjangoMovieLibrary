from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_movie_library.recommend.serializers import RecommendationsResponseSerializer, ReommendationsModelSerializer
from django_movie_library.movie.models import Movie, Genre
from .models import Recommendations
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
import random


class RecommendationsViewSet(viewsets.ModelViewSet):
    queryset = Recommendations.objects.all()
    serializer_class = ReommendationsModelSerializer
    permission_class = [permissions.IsAuthenticated]


@api_view(['POST'])
def get_recommendation(request):
    if request.data['genre'] and request.data['user']:
        genre_name = request.data['genre']
        genre = Genre.objects.filter(name=genre_name).first()

        user_name = request.data['user']
        user = User.objects.filter(username=user_name).first()

        if genre:
            genre_id = genre.id
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        similar_movies_by_genre = list(Movie.objects.filter(genre=genre_id))
        recommendation = random.choice(similar_movies_by_genre)

        Recommendations.objects.create(user=user, recommended_movie=recommendation)

        serializer = RecommendationsResponseSerializer(recommendation)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
