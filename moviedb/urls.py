from django.urls import path, include
from rest_framework import routers
from api.views import MovieViewSet
from api.views import index
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', MovieViewSet)
router.register(r'api/<int:pk>', MovieViewSet)

urlpatterns = [
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
]
