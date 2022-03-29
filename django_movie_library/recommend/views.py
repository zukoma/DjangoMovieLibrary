from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_movie_library.movie.serializers import MovieSerializer
from django_movie_library.recommend.serializers import RecommendMovieSerializer
from django_movie_library.movie.models import Movie, Genre
import random


@api_view(['POST'])
def get_recommendation(request):
    # No need to check if the method is post because we already allow only POST methods in line 10
    if request.method == 'POST':
        genre_name = request.data['genre']
        # TODO correct way to ge tan item is
        # genre = Genre.objects.filter(name=genre_name).first()
        # if genre:
        #   genre_id = genre.id
        genre_id = Genre.objects.filter(name=genre_name)[0].id

        # I would prefer to have a models.Recommendation
        # 

        # Generic comment. As a rule, its not a good idea to put business logic into View
        # Its better to have either model methods or queryset methods
        similar_movies_by_genre = list(Movie.objects.filter(genre=genre_id))
        recommendation = random.choice(similar_movies_by_genre)

        serializer = RecommendMovieSerializer(recommendation)

        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
