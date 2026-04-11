from rest_framework import serializers
from .models import Movie, Favorite

class MovieSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = "__all__"

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return f"http://127.0.0.1:8000/media/{obj.thumbnail}"
        return None

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = "__all__"