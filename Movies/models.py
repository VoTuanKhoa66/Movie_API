from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_day = models.DateField()

class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_day = models.DateField()

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title_movie = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, null=False)
    actors = models.ManyToManyField(Actor, null=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True)

class MovieImage(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=128)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_image', null=False)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review', null=False)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)








