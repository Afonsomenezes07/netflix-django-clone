from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Movie,Favorite
from .serializers import MovieSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = ['title']


    @action(detail=False, methods=['get'])
    def by_category(self, request):

        category_id = request.query_params.get('category')

        movies = Movie.objects.filter(category_id=category_id)

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

class FavoriteViewSet(viewsets.ModelViewSet):

    serializer_class = FavoriteSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)



# Create your views here.
