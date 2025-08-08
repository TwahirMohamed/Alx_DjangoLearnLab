from django.db import models

# Create your models here.
# The Author model has a writer who can have multiple books.
# It has a one-to-many relationship with Book (one author, many books).

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"This is the author called {self.name}"

# The Book model represents an individual book.
# It includes a title, publication year, and a foreign key linking it to an Author.
# The related_name="books" allows reverse access from Author → Book list (author.books).
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"This is an instance for book with the title: {self.title} published on {self.publication_year}by : {self.name}"
    
