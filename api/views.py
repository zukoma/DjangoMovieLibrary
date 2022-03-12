from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Avg


@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    all_movies = Movie.objects.all().order_by('-id')
    return render(request, 'index.html', {'all_movies': all_movies})


def stats_view(request):
    all_movies = Movie.objects.all()
    avg_rating = all_movies.aggregate(Avg('rating'))['rating__avg']
    max_rating = all_movies.order_by('-rating').first()
    low_rating = all_movies.order_by('rating').first()

    data = {'total_movies': len(all_movies),
            'max_rating': max_rating,
            'avg_rating': avg_rating,
            'low_rating': low_rating}

    return render(request, 'stats.html', data)


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

