from django.urls import path
from .views import LibrarianDashboardView
from .views import BookListView, create_book, EditBookView, DeleteBookView
app_name = 'books'


urlpatterns = [
    path('librarian_dashboard/', LibrarianDashboardView.as_view(), name='librarian_dashboard'),
    path('', BookListView.as_view(), name='book_list'),
    path('add/', create_book, name='create_book'),
    path('<int:pk>/edit/', EditBookView.as_view(), name='edit_book'),
    path('<int:pk>/delete/', DeleteBookView.as_view(), name='delete_book'),
]
