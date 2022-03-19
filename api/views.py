from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer, UserAddedBySerializer
from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    all_movies = Movie.objects.all().order_by('-id')
    return render(request, 'index.html', {'all_movies': all_movies})


@api_view(('GET', ))
def stats_view_json(request):
    movie_count = Movie.objects.count()
    avg_rating = Movie.objects.average_rating()
    max_rating = Movie.objects.max_rating()
    low_rating = Movie.objects.low_rating()
    user_with_most_movies = Movie.objects.user_with_most_movies()
    data = {'total_movies': movie_count,
            'max_rating': max_rating,
            'avg_rating': avg_rating,
            'low_rating': low_rating,
            "user_with_most_movies": user_with_most_movies
            }

    return Response(data)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_class = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = [permissions.IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     new_movie = Movie.objects.create(title=data['title'],
    #                                      year=data['year'],
    #                                      rating=data['rating'],
    #                                      notes=data['notes'])
    #     new_movie.save()
    #
    #     for genre in data['genre']:
    #         genre_obj = Genre.objects.get(genre=genre['genre'])
    #         new_movie.genre.add(genre_obj)
    #
    #     serializer = MovieSerializer(new_movie)
    #     return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAddedBySerializer
    permission_class = [permissions.IsAuthenticated]


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, "registration/register.html", context={"form": form})

    form = UserCreationForm
    return render(request, "registration/register.html", context={"form": form})

