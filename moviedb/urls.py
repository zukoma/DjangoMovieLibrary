from django.urls import path, include
from api.views import MovieViewSet, index, register, stats_view
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api', MovieViewSet)
router.register(r'api/<int:pk>', MovieViewSet)

urlpatterns = [
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('stats/', stats_view),
    path('', include(router.urls)),
]
