from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

    # def get_queryset(self):
    #     queryset = self.queryset
    #     name_filter = self.request.query_params.get('name', None)
    #     if name_filter is not None:
    #         queryset = queryset.filter(name__icontains=name_filter)
    #     return queryset

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer