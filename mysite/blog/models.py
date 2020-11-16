from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
	name  = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.TextField()
	date_published = models.DateTimeField(default =timezone.now)
	category = models.CharField(max_length = 200, default = 'uncategorized')
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return f'{self.title} ||| {self.author}'

	def get_absolute_url(self):
		return reverse('home')