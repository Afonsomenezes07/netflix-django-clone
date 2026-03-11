from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class WatchHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    progress = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.movie}"

# Create your models here.
