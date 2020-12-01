from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('name','name')
category_values = []
for i in choices:
	category_values.append(i)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','snippet','category']

		widgets = {
		'category':forms.Select(choices=category_values),
		'snippet':forms.Textarea(),
		}


class UpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','snippet','category']
		
		widgets = {
		'category':forms.Select(choices=category_values),
		'snippet':forms.Textarea(),
		}