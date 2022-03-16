from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Max, Min
from django.contrib.auth.models import User


class MovieQuerySet(models.QuerySet):
    def average_rating(self):
        return self.aggregate(Avg('rating'))['rating__avg']

    def max_rating(self):
        return self.aggregate(Max('rating'))['rating__max']

    def low_rating(self):
        return self.aggregate(Min('rating'))['rating__min']


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(
        default=1900,
        validators=[
            MaxValueValidator(2300),
            MinValueValidator(1900)
        ])
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    notes = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    def rename(self, new_title):
        self.title = new_title
        self.save()

    objects = MovieQuerySet.as_manager()

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)