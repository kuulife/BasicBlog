from django.shortcuts import render
from .models import Post,Category
from .forms import PostForm,UpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

def CategoryView(request,cats):
	category_values = Post.objects.filter(category=cats.replace('-',' '))
	cat_menu = Category.objects.all()
	context = {'cats':cats,'category_values':category_values,'cat_menu':cat_menu}
	return render(request, 'blog/category.html',context)


class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'
	cats = Category.objects.all()
	ordering = ['-posted']

	def get_context_data(self,*args,**kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		context['cat_menu'] = cat_menu
		return context

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail_post.html'

	def get_context_data(self,*args,**kwargs):
		cat_menu = Category.objects.all()
		context = super(PostDetailView,self).get_context_data(*args,**kwargs)
		context['cat_menu'] = cat_menu
		return context


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/add_post.html'

class PostCategoryView(CreateView):
	model = Category
	template_name = 'blog/add_category.html'
	fields = '__all__'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	template_name = 'blog/update_post.html'
	form_class = UpdateForm

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




