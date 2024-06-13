from django.urls import path
from Movies import views

urlpatterns = [
    path('genre/', views.GenreAPIView.as_view()),
    path('genre/<slug:id_slug>/', views.GenreDetailAPIView.as_view()),

    path('actor/', views.ActorAPIView.as_view()),
    path('actor/<slug:id_slug>/', views.ActorDetailAPIView.as_view()),

    path('director/', views.DirectorAPIView.as_view()),
    path('director/<slug:id_slug>/', views.DirectorDetailAPIView.as_view()),

    path('movie/<slug:id_movie_slug>/images/', views.MovieImageAPIView.as_view()),
    path('movie/<slug:id_movie_slug>/images/<slug:id_slug>/', views.MovieImageDetailAPIView.as_view()),

    path('movie/', views.MovieAPIView.as_view()),
    path('movie/<slug:id_slug>/', views.MovieDetailAPIView.as_view()),

    path('movie/<slug:id_movie_slug>/reviews/', views.ReviewAPIView.as_view()),
]
