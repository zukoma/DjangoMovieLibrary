from django.urls import path, include
from django_movie_library.movie.views import MovieViewSet, index, register, UserViewSet
from django_movie_library.genre.views import GenreViewSet
from django_movie_library.ratings.views import RatingsViewSet
from django_movie_library.recommend.views import RecommendationsViewSet
from rest_framework import routers
from django_movie_library.recommend.views import get_recommendation


router = routers.DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/movies<int:pk>', MovieViewSet)

router.register(r'api/genres', GenreViewSet)
router.register(r'api/genres<int:pk>', GenreViewSet)

router.register(r'api/ratings', RatingsViewSet)
router.register(r'api/ratings<int:pk>', RatingsViewSet)

router.register(r'api/recommendations', RecommendationsViewSet)
router.register(r'api/recommendations<int:pk>', RecommendationsViewSet)

router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('', index),
    path('', include(router.urls)),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('recommend/', get_recommendation, name='recommendation')
]
