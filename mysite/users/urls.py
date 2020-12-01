from django.urls import path
from .views import UserRegisterView,UserUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(),name='profile')
]
