from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"This is the author called {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"This is an instance for book with the title: {self.title} published on {self.publication_year}by : {self.name}"
    
