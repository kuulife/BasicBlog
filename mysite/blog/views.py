from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (DetailView ,
	 ListView , 
	 CreateView, 
	 UpdateView, 
	 DeleteView,
 )
from django.contrib import messages
from .models import Post, Category
from .forms import PostForm , PostUpdateForm

class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'
	ordering = ['-date_published']

class PostDetialView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostCreatView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/add_post.html'

class PostCategoryView(CreateView):
	model = Category
	template_name = 'blog/add_category.html'
	fields = '__all__'

class PostUpdateView(UpdateView):
	model = Post
	form_class = PostUpdateForm
	template_name = 'blog/update_post.html'

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')






