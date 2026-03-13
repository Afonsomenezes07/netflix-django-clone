from rest_framework import serializers
from .models import Movie, Favorite

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = "__all__"