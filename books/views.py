from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from borrowings.models import Borrow
from .models import Book
from .forms import BookForm
from accounts.mixins import LibrarianRequiredMixin


def is_librarian(user):
    return user.is_authenticated and user.is_librarian


class LibrarianDashboardView(LibrarianRequiredMixin, TemplateView):
    template_name = 'books/librarian_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['borrowed_books'] = Borrow.objects.filter(returned_at__isnull=True)
        return context





class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'




@login_required
@user_passes_test(is_librarian)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

class EditBookView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/edit_book.html'
    success_url = reverse_lazy('books:book_list')

    def test_func(self):
        return self.request.user.is_librarian


class DeleteBookView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_url = reverse_lazy('books:book_list')

    def test_func(self):
        return self.request.user.is_librarian







