from django.urls import path
from .views import HomeView , PostDetialView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetialView.as_view(), name='post-detail'),
]	