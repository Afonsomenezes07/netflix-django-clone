from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Movie,Favorite
from .serializers import MovieSerializer, FavoriteSerializer


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = ['title']

    @action(detail=False, methods=['get'])
    def by_category(self, request):

        category_id = request.query_params.get('category')

        movies = Movie.objects.filter(category_id=category_id)

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

class FavoriteViewSet(viewsets.ModelViewSet):

    queryset = Favorite.objects.all()

    serializer_class = FavoriteSerializer

# Create your views here.
