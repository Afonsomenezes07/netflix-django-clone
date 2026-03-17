from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from categories.models import Category
from watch_history.models import WatchHistory
from .models import Movie,Favorite
from django.db.models import Count
from .serializers import MovieSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

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


class FeaturedMoviesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        movies = Movie.objects.filter(featured=True)

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class WatchMovieView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        movie = get_object_or_404(Movie, id=pk)

        # salva histórico
        WatchHistory.objects.create(
            user=request.user,
            movie=movie
        )

        serializer = MovieSerializer(movie)

        return Response(serializer.data)


class TopMoviesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        top_movies = (
            WatchHistory.objects.values("movie")
            .annotate(total=Count("movie"))
            .order_by("-total")[:10]
        )

        movie_ids = [item["movie"] for item in top_movies]

        movies_dict = {movie.pk: movie for movie in Movie.objects.filter(id__in=movie_ids)}
        ordered_movies = [movies_dict[movie_id] for movie_id in movie_ids if movie_id in movies_dict]

        serializer = MovieSerializer(ordered_movies, many=True)

        return Response(serializer.data)
# Create your views here.
