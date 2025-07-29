from rest_framework import serializers
from .models import Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    def get_days_since_created(self, obj):
        delta = datetime.now().date() - obj.created_at.date()
        return delta.days