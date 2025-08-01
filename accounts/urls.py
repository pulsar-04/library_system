from django.urls import path
from .views import CustomLoginView, RegisterView, UserLogoutView, edit_profile_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
path("edit-profile/", edit_profile_view, name="edit_profile"),


]
