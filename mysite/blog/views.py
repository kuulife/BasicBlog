from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import (DetailView ,
	 ListView , 
	 CreateView, 
	 UpdateView, 
	 DeleteView,
 )
from django.contrib import messages
from .models import Post, Category
from .forms import PostForm , PostUpdateForm
from django.http import HttpResponseRedirect


def LikeView(request,pk):
	post = get_object_or_404(Post,id = request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('post-detail',args = [str(pk)]))

class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'
	cats  = Category.objects.all()
	ordering = ['-date_published']

	def get_context_data(self, *args , **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView,self).get_context_data(*args , **kwargs)
		context['cat_menu'] = cat_menu
		return context


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category = cats)
	context = {
		'category_posts':category_posts,
		'cats':cats,
	}
	return render(request, 'blog/categories.html',context)

class PostDetialView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

	def get_context_data(self, *args , **kwargs):
		
		context = super(PostDetialView,self).get_context_data(*args , **kwargs)

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		context['total_likes'] = total_likes
		return context


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


def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	context = {
		'cat_menu_list':cat_menu_list,
	}
	return render(request, 'blog/categories_list.html',context)




