
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Título del libro
    description = models.TextField()         # Descripción del libro

    def __str__(self):
        return f'{self.title}, {self.description}'

