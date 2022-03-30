from django.db import models
from django.contrib.auth.models import User


class Recommendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_movie = models.ForeignKey("movie.Movie", on_delete=models.CASCADE)
    recommended_at = models.DateTimeField(auto_now_add=True, )
