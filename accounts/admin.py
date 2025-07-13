from django.contrib import admin



# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_librarian', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_librarian', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_librarian', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_librarian', 'is_staff', 'is_superuser'),
        }),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
