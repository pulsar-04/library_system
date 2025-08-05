from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Borrow

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrowed_at', 'returned_at')
    list_filter = ('borrowed_at', 'returned_at')
    search_fields = ('book__title', 'user__username')

