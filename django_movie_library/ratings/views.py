from .models import Ratings
from .serializers import RatingsSerializer
from rest_framework import viewsets, permissions


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    permission_class = [permissions.IsAuthenticated]
