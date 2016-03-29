from django.db import models
from django.utils import timezone

class BookDetails (models.Model):
    title = models.CharField (max_length=100)
    auth = models.CharField (max_length=50)
    loc = models.CharField (max_length=20)
    genre = models.CharField (max_length=50)

    def __str__(self):
        return self.title