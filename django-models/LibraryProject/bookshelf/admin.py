from django.contrib import admin
from .models import Book  # This imports the model from models.py

admin.site.register(Book) 
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # Columns in list view
    list_filter = ('publication_year',)                      # Sidebar filters
    search_fields = ('title', 'author')   