from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'index.html', {'all_movies': all_movies})


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = [permissions.IsAuthenticated]


# class MovieRequests(APIView):
#
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class MovieRequestsPk(APIView):
#     def get_movie(self, pk):
#         try:
#             return Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         movie = self.get_movie(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         movie = self.get_movie(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk, format=None):
#         movie = self.get_movie(pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
