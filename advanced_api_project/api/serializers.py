from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


# BookSerializer:
# - Serializes all fields of the Book model.
# - Includes custom validation to ensure the publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer:
# - Serializes the author's name.
# - Uses a nested BookSerializer to serialize related books dynamically.
# - books is read-only here (to prevent inline creation in this example).
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested representation
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = '__all__'
    
    def get_days_since_created(self, obj):# customizing serializers
        delta = datetime.now().date() - obj.created_at.date()
        return delta.days