from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import  reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = RichTextField(blank=True, null=True)
	posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.CharField(max_length = 200, default = 'uncotegorized')
	likes = models.ManyToManyField(User, related_name='like_post')

	def total_llikes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home')