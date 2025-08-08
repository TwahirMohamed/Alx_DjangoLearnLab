from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author 
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.
class CustomBookListView(generics.ListAPIView):
# to retrieve all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Retrieve single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Adding a new book 
class BookCreateView(generics.CreateAPIView):
    model = Book
    serializer_class = BookSerializer
    fields = ['title', 'publication_year', 'author']

    # function to perform book creatiion
    def perform_create(self, serializer):
        return super().perform_create(serializer)


# for modifying an existing book.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class  BookDeleteView(generics.DeleteAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
