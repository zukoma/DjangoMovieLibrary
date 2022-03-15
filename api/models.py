from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Max, Min


class MovieManager(models.Manager):
    def average_rating(self):
        return super().get_queryset().aggregate(Avg('rating'))['rating__avg']

    def max_rating(self):
        return super().get_queryset().aggregate(Max('rating'))['rating__max']

    def low_rating(self):
        return super().get_queryset().order_by('rating').first().rating

    def max_rated_movie(self):
        pass


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

    objects = MovieManager()