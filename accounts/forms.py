from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser

class AppUserRegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', "first_name", "last_name"]
        help_texts = {
            'username': None,
        }