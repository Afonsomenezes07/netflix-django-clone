from rest_framework import viewsets, filters
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = ['title']
    
# Create your views here.
