# pyrefly: ignore [missing-import]
from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT,
        related_name='movies'
        )
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name='movies'
        )
    resume = models.TextField( null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    poster_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


    @property
    def formatted_duration(self):
        if self.duration:
            try:
                duration = int(self.duration)
                hours = duration // 60
                minutes = duration % 60
                return f'{hours}h {minutes}m' if hours else f'{minutes}m'
            except (ValueError, TypeError):
                return str(self.duration)
        return None