from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
# Syntax
# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# Signal to automatically create UserProfile on user creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Author(models.Model):
    """Table for the author"""
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Table for the book"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

    def __str__(self):
        return self.name


class Library(models.Model):
    """Table for the Library"""
    name = models.CharField(max_length=80)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return self.name


class Librarian(models.Model):
    """Table for the Librarian"""
    name = models.CharField(max_length=80)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name