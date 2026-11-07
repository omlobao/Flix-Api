from django.db import models


NATIONALITY_CHOICES = (
    ('American', 'American'),
    ('British', 'British'),
    ('Canadian', 'Canadian'),
    ('French', 'French'),
    ('German', 'German'),
    ('Indian', 'Indian'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
    ('Mexican', 'Mexican'),
    ('Spanish', 'Spanish'),
    ('Other', 'Other'),
    )


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES,
                                   blank=True, null=True)
    
    
    def __str__(self):
        return self.name