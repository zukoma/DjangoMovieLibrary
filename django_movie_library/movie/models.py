from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.contrib.auth.models import User
from django_movie_library.genre.models import Genre
from django_movie_library.ratings.models import Ratings

ratings = models.ForeignKey('django_movie_library.genre.Genre', on_delete=models.CASCADE)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(
        default=1900,
        validators=[
            MaxValueValidator(2300),
            MinValueValidator(1900)
        ])
    notes = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    added_at = models.DateTimeField(auto_now_add=True, )

    def rename(self, new_title):
        self.title = new_title
        self.save()

    def get_rating(self):
        return Ratings.objects.filter(movie=self).aggregate(Avg('rating'))['rating__avg']

    def get_rating_count(self):
        return Ratings.objects.filter(movie=self).count()

    def __str__(self):
        return self.title
