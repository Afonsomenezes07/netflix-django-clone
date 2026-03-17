from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Movie(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    thumbnail = models.ImageField(upload_to="thumbnails/")

    video = models.FileField(upload_to="movies/")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    year = models.IntegerField(default=2000)

    duration = models.IntegerField(help_text="Duration in minutes", default=120)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.movie}"

# Create your models here.
