from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    imgPath = models.CharField(max_length=100)
    duration = models.IntegerField()
    genre = models.JSONField()
    language = models.CharField(max_length=100)
    mpaaRating = models.JSONField()
    userRating = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
