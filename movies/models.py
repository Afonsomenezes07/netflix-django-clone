from django.db import models
from categories.models import Category

class Movie(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    thumbnail = models.ImageField(upload_to="thumbnails/")

    video = models.FileField(upload_to="movies/")

    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# Create your models here.
