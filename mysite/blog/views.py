from django.shortcuts import render
from .models import Post,Category
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

def CategoryView(request,cats):

	context = {'cats':cats}
	return render(request, 'blog/category.html',context)

class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'
	ordering = ['-posted']

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail_post.html'

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/add_post.html'

class CategoryCreateView(LoginRequiredMixin,CreateView):
	model = Category
	template_name = 'blog/add_category.html'
	fields = "__all__"


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	template_name = 'blog/update_post.html'
	fields = ['title','content','category']

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

def about(request):
	return render(request, 'blog/about.html')




