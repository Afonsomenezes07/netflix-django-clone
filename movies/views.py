from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from categories.models import Category
from watch_history.models import WatchHistory
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

        serializer = self.get_serializer(movies, many=True)

        return Response(serializer.data)

class FavoriteViewSet(viewsets.ModelViewSet):

    serializer_class = FavoriteSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class HomePageView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        data = {}

        categories = Category.objects.all()

        for category in categories:

            movies = Movie.objects.filter(category=category)[:10]

            serializer = MovieSerializer(movies, many=True)

            data[category.name] = serializer.data

        return Response(data)


class RecommendationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        history = WatchHistory.objects.filter(user=user)

        categories = history.values_list("movie__category", flat=True).distinct()

        movies = Movie.objects.filter(category__in=categories).distinct()[:10]

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
# Create your views here.
