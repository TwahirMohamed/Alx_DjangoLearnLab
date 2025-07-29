from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
    #In this example, the BookListCreateAPIView inherits from the ListCreateAPIView class provided by DRF. The queryset attribute is set to Book.objects.all(), which fetches all instances of the Book model. The get_queryset() method is overridden to add a dynamic filter based on the name query parameter.
