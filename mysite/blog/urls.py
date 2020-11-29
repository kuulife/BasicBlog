from django.urls import path
from .views import (
	HomeView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    CategoryCreateView,
    CategoryView,
)
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name='home' ),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail' ),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update' ),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete' ),
    path('post/new/',PostCreateView.as_view(),name='post-new' ),
    path('category-new/',CategoryCreateView.as_view(),name='add-category' ),
    path('about/', views.about, name='about'),
    path('category/<str:cats>/', CategoryView, name='category'),

]
