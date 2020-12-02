from django.contrib import admin
from django.urls import path, include
from users.views import UserRegisterView,UserUpdateView,PasswordsChangeView
from users import views


urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(),name='profile'),
    path('password-success/', views.password_success,name='password-success'),
    path('password/',PasswordsChangeView.as_view(template_name='users/change_password.html')),
    ]