from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.decorators import librarian_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'home.html'

def is_librarian(user):
    return user.is_authenticated and user.is_librarian

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'books/librarian_dashboard.html')

