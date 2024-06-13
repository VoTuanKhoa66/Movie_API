from rest_framework import views
from django.http import Http404
from .serializer import *
from .models import *
from WEB_MOVIE.helpers import custom_response, parse_request

# Create your views here.
class GenreAPIView(views.APIView):
    def get(self, request):
        try:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return custom_response('Get all genre successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get all genre failed!', 'Error', None, 400)
    
    def post(self, request):
        data = parse_request(request)
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create genre successfully!', 'Success', serializer.data, 200)
        else:
            return custom_response('Create genre failed!', 'Error', serializer.errors, 400)

class GenreDetailAPIView(views.APIView):
    def get_object(self,id_slug):
        try:
            return Genre.objects.get(pk=id_slug)
        except:
            raise Http404
        
    def get(self, request, id_slug):
        try: 
            genre = self.get_object(id_slug)
            serializer = GenreSerializer(genre)
            return custom_response('Get genre successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get genre failed!', 'Error', 'Genre not found!', 400)
        
    def put(self, request, id_slug):
        try:
            genre = self.get_object(id_slug)
            data = parse_request(request)
            serializer = GenreSerializer(genre, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update genre successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update genre failed!', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update genr failed!', 'Error', 'Genre not found!', 400)
        
    def delete(self, request, id_slug):
        try:
            genre = self.get_object(id_slug)
            genre.delete()
            return custom_response('Delete genre successfully!', 'Success', {'Genre_id':id_slug}, 200)
        except:
            return custom_response('Update genr failed!', 'Error', 'Genre not found!', 400)
        


class ActorAPIView(views.APIView):
    def get(self, request):
        try:
            actors = Actor.objects.all()
            serializer = ActorSerializer(actors, many=True)
            return custom_response('Get actor successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get actor failed!', 'Error', None, 400)

    def post(self, request):
        data = parse_request(request)
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create actor successfully!', 'Success', serializer.data, 200)
        else:
            return custom_response('Create actor failed!', 'Error', serializer.errors, 400)
        
class ActorDetailAPIView(views.APIView):
    def get_object(self, id_slug):
        try:
            return Actor.objects.get(pk=id_slug)
        except: 
            raise Http404
    
    def get(self, request, id_slug):
        try:
            actor = self.get_object(id_slug)
            serializer = ActorSerializer(actor)
            return custom_response('Get actor successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get actor failed!', 'Error', 'Actor not found!', 400)
        
    def put(self, request, id_slug):
        try:
            actor = self.get_object(id_slug)
            data = parse_request(request)
            serializer = ActorSerializer(actor, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update actor successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update actor failed!', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update actor failed!', 'Error', 'Actor not found!', 400)
        
    def delete(self, request, id_slug):
        try:
            actor = self.get_object(id_slug)
            actor.delete()
            return custom_response('Delete actor successfully!', 'Success', {'actor_id':id_slug}, 200)
        except:
            return custom_response('Delete actor failed!', 'Error', 'Actor not found!', 400)
        
class DirectorAPIView(views.APIView):
    def get(self, request):
        try:
            directors = Director.objects.all()
            serializer = DirectorSerializer(directors, many=True)
            return custom_response('Get director successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get director failed!', 'Error', None, 400)
    
    def post(self, request):
        data = parse_request(request)
        serializer = DirectorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create director successfully!', 'Success', serializer.data, 200)
        else:
            return custom_response('Create director failed!', 'Error', serializer.errors, 400)
        
class DirectorDetailAPIView(views.APIView):
    def get_object(self, id_slug):
        try:
            return Director.objects.get(pk=id_slug)
        except:
            raise Http404
        
    def get(self, request, id_slug):
        try:
            director = self.get_object(id_slug)
            serializer = DirectorSerializer(director)
            return custom_response('Get director successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get director failed!', 'Error', 'Director not found!', 400)
        
    def put(self, request, id_slug):
        try:
            director = self.get_object(id_slug)
            data = parse_request(request)
            serializer = DirectorSerializer(director, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update director successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update director failed!', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update director failed!', 'Error', 'Director not found!', 400)
        
    def delete(self, request, id_slug):
        try: 
            director = self.get_object(id_slug)
            director.delete()
            return custom_response('Delete director successfully!', 'Success', {'director_id':id_slug}, 200)
        except:
            return custom_response('Delete director failed!', 'Error', 'Director not found!', 400)
            

class MovieAPIView(views.APIView):
    def get(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return custom_response('Get movies successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get movies failed!', 'Error', None, 400)
        
    def post(self , request):
        data = parse_request(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create movie successfully!', 'Success', serializer.data, 200)
        else:
            return custom_response('Create movie failed!', 'Error', serializer.errors, 400)

class MovieDetailAPIView(views.APIView):
    def get_object(self, id_slug):
        try:
            return Movie.objects.get(pk=id_slug)
        except:
            raise Http404
        
    def get(self, request , id_slug):
        try:
            movie = self.get_object(id_slug)
            serializer = MovieSerializer(movie)
            return custom_response('Get movie successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get movie failed!', 'Error', 'Movie not found!', 400)
    
    def put(self, request, id_slug):
        try:
            movie = self.get_object(id_slug)
            data = parse_request(request)
            serializer = MovieSerializer(movie, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update movie successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update movie failed!', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update movie failed!', 'Error', 'Moive not found!', 400)
        
    def delete(self, request, id_slug):
        try:
            movie = self.get_object(id_slug)
            movie.delete()
            return custom_response('Delete movie successfully!', 'Success', {'movie_id':id_slug}, 200)
        except:
            return custom_response('Delete movie failed!', 'Error', 'Movie not found!', 400)

class MovieImageAPIView(views.APIView):
    def get(self, request, id_movie_slug):
        try:
            movie_image = MovieImage.objects.filter(movie_id=id_movie_slug).all()
            serializer = MovieImageSerializer(movie_image, many=True)
            return custom_response('Get all movie images successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get all movie images falied!', 'Error', None, 400)
        
    def post(self, request, id_movie_slug):
        try:
            data = parse_request(request)
            movie = Movie.objects.get(id=id_movie_slug)
            movie_image = MovieImage(
                movie_id = movie,
                image_url = data['image_url']
            )
            movie_image.save()
            serializer = MovieImageSerializer(movie_image)
            return custom_response('Create movie image successfully!', 'Success', serializer.data, 200)
        except Exception as e:
            return custom_response('Create movie image failed!', 'Error', {'Error':str(e)}, 400)
    
class MovieImageDetailAPIView(views.APIView):
    
    def get_object(self, id_slug):
        try:
            return MovieImage.objects.get(id=id_slug)
        except:
            raise Http404

    def get_object_with_movie_id(self, id_movie_slug, id_slug):
        try:
            return MovieImage.objects.get(id_movie_slug=id_movie_slug, id_slug=id_slug)
        except:
            raise Http404

    def get(self, request, id_movie_slug, id_slug):
        try:
            movie_image = self.get_object(id_slug)
            serializer = MovieImageSerializer(movie_image)
            return custom_response('Get movie image successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get movie image successfully!', 'Error', 'Movie image not found!', 400)

    def put(self, request, id_movie_slug, id_slug):
        try:
            data = parse_request(request)
            movie_image = self.get_object_with_movie_id(id_movie_slug, id_slug)
            serializer = MovieImageSerializer(movie_image, data=data)
            if serializer.is_valid():
                serializer.save
                return custom_response('Update movie image successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update movie image failed!', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update movie image failed!', 'Error', 'Movie image not found!', 400)

    def delete(self, request, id_movie_slug, id_slug):
        try: 
            movie_image = self.get_object_with_movie_id(id_movie_slug, id_slug)
            movie_image.delete()
            return custom_response('Delete movie image successfully!', 'Success', {'id_movie':id_slug}, 200)
        except:
            return custom_response('Delete movie image failed!', 'Error', 'Movie image not found!', 400)

class ReviewAPIView(views.APIView):
    def get(self, request, id_movie_slug):
        try:
            reviews = Review.objects.filter(movie_id=id_movie_slug).all()
            serializer = ReviewSerializer(reviews, many=True)
            return custom_response('Get all review successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get all review failed!', 'Success', None, 400)

    def post(self, request, id_movie_slug):
        try:
            data = parse_request(request)
            movie = Movie.objects.get(id=id_movie_slug)
            user = User.objects.get(id=data['user_id'])
            review = Review(
                movie_id = movie,
                user = user,
                rating = data['rating'],
                content = data['content']
            )
            review.save()
            serializer = ReviewSerializer(review)
            return custom_response('Create review successfully!', 'Success', serializer.data, 200)
        except Exception as e:
            return custom_response('Create review failed!', 'Error', {'Error':str(e)}, 400)
        

                
