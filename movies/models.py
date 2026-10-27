from django.db import models

class Movie(models.Model):


    GENRES_CHOICES = {
    
            ("Action","Action"),
            ("Comedy","Comedy"),
            ("Thriller","Thriller"),
            ("Sci-fi","Sci-fi"),
        }

    LANGUAGE_CHOICES = {
    
            ("Malayalam","Malayalam"),
            ("Hindi","Hindi"),
            ("Kannada","Kannada"),
            ("English","English"),
            ("Tamil","Tamil"),
        }
    

    title = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    genres = models.CharField(max_length=50,choices=GENRES_CHOICES,default="Action")

    ratings = models.DecimalField(max_digits=3,decimal_places=2)

    language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="Malayalam")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):

        return self.title
    
