from rest_framework import serializers
from .models import Book, User
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField() # Customization
    class Meta:
        model = Book
        fields = '__all__'
    def get_days_since_created(self, obj):# customizing serializers
        delta = datetime.now().date() - obj.created_at.date()
        return delta.days

class UserSerializer(serializers.ModelSerializer):
    """
    A custom serializer for a User model that includes full_name field calculated from the first_name and last_name fields in the model.
    """
    days_since_created = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'full_name']

        def get_full_name(self, obj):
            return f"The full name: {obj.first_name} {obj.last_name}".strip()
        
