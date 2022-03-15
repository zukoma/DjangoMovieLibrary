from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.decorators import api_view


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

    data = {'total_movies': movie_count,
            'max_rating': max_rating,
            'avg_rating': avg_rating,
            'low_rating': low_rating}

    return Response(data)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
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

