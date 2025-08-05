from django.contrib.auth import logout
from django.views import generic
from .forms import AppUserRegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required

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

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.next_page)

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_librarian:
             #if hasattr(request.user, 'profile') and request.user.profile.is_librarian:
                return redirect('books:librarian_dashboard')
        return super().get(request, *args, **kwargs)



@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("books:book_list")  # Ще го създадем
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "accounts/edit_profile.html", {"form": form})


