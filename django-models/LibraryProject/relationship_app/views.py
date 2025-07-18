from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.
def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""
    model = Book
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        context['books'] = self.object.books.all()
        return context

