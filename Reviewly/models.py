from django.db import models

from movies.models import Movie

from django.contrib.auth.models import User

class Review(models.Model):

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    message = models.TextField()

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    ratings = models.DecimalField(max_digits=3,decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    class Meta:

        unique_together = ("movie","created_by")

    def __str__(self):
        return f"{self.movie} - {self.message}"





