from django.urls import path
from . import views
from .views import (
	HomeView,PostDetailView,
	PostCreateView,PostUpdateView,
	PostDeleteView,PostCategoryView,
    CategoryView,LikeView,
    AddCommentView,
)



urlpatterns = [
    path('',HomeView.as_view(),name='home' ),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail' ),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update' ),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete' ),
    path('post/new/',PostCreateView.as_view(),name='post-new' ),
    path('categoryAdd/',PostCategoryView.as_view(),name='category-new' ),
    path('category/<str:cats>/',CategoryView,name='category' ),
    path('like/<int:pk>/',LikeView,name='like-post' ),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/add-comment/', AddCommentView.as_view(), name='add-comment'),
]
