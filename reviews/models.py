from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'A nota deve ser maior ou igual a 1'),
            MaxValueValidator(5, 'A nota deve ser menor ou igual a 5'),
        ]
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.movie)

        
