from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from django.contrib.auth.decorators import user_passes_test


from books.models import Book
from borrowings.models import Borrow
from borrowings.forms import ReturnBookForm
from django.utils import timezone


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

    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            borrow.returned_at = now()
            borrow.book.is_available = True
            borrow.book.save()
            borrow.save()
            messages.success(request, "Book returned successfully.")
            return redirect('borrowings:your_books')
    else:
        form = ReturnBookForm()

    return render(request, 'borrowings/return_book.html', {
        'form': form,
        'borrow': borrow,
    })



@user_passes_test(lambda u: u.is_librarian)
def force_return(request, book_id):
    borrow = get_object_or_404(Borrow, book_id=book_id, returned_at__isnull=True)
    borrow.returned_at = timezone.now()
    borrow.save()

    book = borrow.book
    book.is_available = True
    book.save()

    return redirect('books:librarian_dashboard')
















