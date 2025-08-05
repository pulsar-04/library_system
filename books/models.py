from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title
