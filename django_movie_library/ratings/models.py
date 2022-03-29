from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey("movie.Movie", on_delete=models.CASCADE)
    rating = models.IntegerField(
        # TODO maybe no need for default rating
        # TODO what about default value 0 when the min value is 1?
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
