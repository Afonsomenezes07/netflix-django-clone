from rest_framework import viewsets, filters
from .models import Movie,Favorite
from .serializers import MovieSerializer, FavoriteSerializer

class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = ['title']

class FavoriteViewSet(viewsets.ModelViewSet):

    queryset = Favorite.objects.all

    serializer_class = FavoriteSerializer
    
# Create your views here.
