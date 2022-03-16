from django.urls import path, include
from api.views import MovieViewSet, GenreViewSet, index, register, stats_view_json, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/movies<int:pk>', MovieViewSet)
router.register(r'api/genres', GenreViewSet)
router.register(r'api/genres<int:pk>', GenreViewSet)
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('', index),
    path('', include(router.urls)),
    path('stats/', stats_view_json),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
