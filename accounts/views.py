# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import AppUserRegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import TemplateView

class RegisterView(generic.CreateView):
    form_class = AppUserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        if self.request.user.is_librarian:
            return reverse('books:librarian_dashboard')
        return reverse('home')


class UserLogoutView(LogoutView):
    next_page = 'home'


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile') and request.user.profile.is_librarian:
                return redirect('books:librarian_dashboard')
        return super().get(request, *args, **kwargs)





