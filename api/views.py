from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets, permissions
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    all_movies = Movie.objects.all().order_by('-id')
    return render(request, 'index.html', {'all_movies': all_movies})


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = [permissions.IsAuthenticated]
