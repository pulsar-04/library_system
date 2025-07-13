# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import AppUserRegisterForm
from django.urls import reverse_lazy

def login_view(request):
    return HttpResponse("<h2>Login page (coming soon)</h2>")

class RegisterView(generic.CreateView):
    form_class = AppUserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
