from .models import *
from rest_framework import serializers

class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    birth_day = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Actor
        fields = '__all__'
        
class DirectorSerializer(serializers.ModelSerializer):
    birth_day = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    movie_image = MovieImageSerializer(many=True, read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    release_date = serializers.DateField(format="%d/%m/%Y")
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, write_only=True)
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True, write_only=True)
    genres_display = GenreSerializer(source='genres', many=True, read_only=True)
    actors_display = ActorSerializer(source='actors', many=True, read_only=True)
    director_display = ActorSerializer(source='director',read_only=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_movie',
            'description',
            'release_date',
            'genres',
            'actors',
            'director',
            'movie_image',
            'review',
            'genres_display',
            'actors_display',
            'director_display'
        )


