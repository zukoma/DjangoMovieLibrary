from .models import Genre
from .serializers import GenreSerializer
from rest_framework import viewsets, permissions


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_class = [permissions.IsAuthenticated]
