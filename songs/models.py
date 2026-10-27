from django.db import models
from django.contrib.auth.models import User

from movies.models import Movie

class Songg(models.Model):

    title = models.CharField(max_length=100)

    duration = models.CharField( null=True,
    blank=True,
    help_text="Duration in seconds")

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    singer = models.CharField(max_length=100)

    track_number = models.PositiveIntegerField(null=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):

        last_objcect = Songg.objects.filter(movie=self.movie).last()

        if last_objcect:

            self.track_number = last_objcect.track_number + 1

        else:

            self.track_number = 1

        return super().save(*args,**kwargs)    


