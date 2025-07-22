from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'home.html'

def is_librarian(user):
    return user.is_authenticated and user.is_librarian

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'books/librarian_dashboard.html')


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# def is_librarian(user):
#     return user.is_authenticated and user.is_librarian

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







