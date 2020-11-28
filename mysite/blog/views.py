from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)


class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'
	ordering = ['-posted']

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail_post.html'

class PostCreateView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/add_post.html'


class PostUpdateView(UpdateView):
	model = Post
	template_name = 'blog/update_post.html'
	fields = ['title','content']

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = '/'

def about(request):
	return render(request, 'blog/about.html')




