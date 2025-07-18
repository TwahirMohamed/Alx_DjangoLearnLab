from django.db import models

# Create your models here.
# Syntax
# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
class Author(models.Model):
    """Table for the author"""
    name = models.CharField(max_length=80)


class Book(models.Model):
    """Table for the book"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')


class Library(models.Model):
    """Table for the Library"""
    name = models.CharField(max_length=80)
    books = models.ManyToManyField(Book, related_name='library')


class Librarian(models.Model):
    """Table for the Librarian"""
    name = models.CharField(max_length=80)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)