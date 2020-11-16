from django.urls import path
from .views import (
	HomeView,
	PostDetialView, 
	PostCreatView, 
	PostUpdateView,
	PostDeleteView,
	PostCategoryView,
	CategoryView,
	CategoryListView,
)

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetialView.as_view(), name='post-detail'),
    path('post_add/', PostCreatView.as_view(), name='post-add'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post_add_category/', PostCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/',CategoryView, name = 'category'),
    path('category_list/',CategoryListView, name = 'category-list'),
]	