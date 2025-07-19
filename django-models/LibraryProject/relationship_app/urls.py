from django.urls import path
from .views import book_list, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    path('books/', book_list, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
