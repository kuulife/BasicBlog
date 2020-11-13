from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import Post

class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'

class PostDetialView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'