from django import forms
from .models import Post , Category


choices = Category.objects.all().values_list('name','name')
choices_list = []
for i in choices:
	choices_list.append(i)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'content')

		widgets ={
		'category':forms.Select(choices=choices_list)
		}

class PostUpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'category')
		widgets ={
		'category':forms.Select(choices=choices_list)
		}
