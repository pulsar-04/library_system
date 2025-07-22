from django.urls import path
from . import views

app_name = 'borrowings'

urlpatterns = [
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('my-books/', views.your_borrowed_books, name='your_books'),
    path('return/<int:borrow_id>/', views.return_book, name='return_book'),
]
