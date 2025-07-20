from django.urls import path
from .views import book_list, LibraryDetailView, user_login, user_logout, register, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.book_list, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'),name='logout'),
    path('register/', views.register, name='register'),
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),

    # Roles url
    path('admin-page/', admin_view, name='admin_view'),
    path('librarian-page/', librarian_view, name='librarian_view'),
    path('member-page/', member_view, name='member_view'),
]
