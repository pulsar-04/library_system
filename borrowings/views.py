from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now


from books.models import Book
from borrowings.models import Borrow


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if not book.is_available:
        messages.error(request, "This book is already borrowed.")
        return redirect('books:book_list')

    already_borrowed = Borrow.objects.filter(user=request.user, book=book, returned_at__isnull=True).exists()
    if already_borrowed:
        messages.warning(request, "You have already borrowed this book.")
        return redirect('books:book_list')

    Borrow.objects.create(user=request.user, book=book)
    book.is_available = False
    book.save()

    messages.success(request, "Book borrowed successfully.")
    return redirect('books:book_list')


@login_required
def your_borrowed_books(request):
    borrowed_books = Borrow.objects.filter(user=request.user, returned_at__isnull=True)
    return render(request, 'borrowings/borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id, user=request.user, returned_at__isnull=True)
    borrow.returned_at = now()
    borrow.book.is_available = True
    borrow.book.save()
    borrow.save()
    return redirect('borrowings:your_books')
