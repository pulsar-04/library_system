from django.urls import path
from .views import librarian_dashboard

urlpatterns = [
    path('librarian_dashboard/', librarian_dashboard, name='librarian_dashboard'),
]
