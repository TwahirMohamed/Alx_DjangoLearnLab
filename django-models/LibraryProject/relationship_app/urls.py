from django.urls import path
from .views import book_list, LibraryDetailView, user_login, user_logout, register
from . import views

urlpatterns = [
    path('books/', views.book_list, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
