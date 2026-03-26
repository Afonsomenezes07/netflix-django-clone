from rest_framework import serializers
from .models import WatchHistory
from movies.serializers import MovieSerializer


class WatchHistorySerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)

    class Meta:
        model = WatchHistory
        fields = "__all__"
