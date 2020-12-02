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

class Profile(models.Model):
	user  = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
	profile_image = models.ImageField(null = True,blank = True, upload_to = 'images-profile/')
	instagram_urls = models.CharField(max_length = 200, null = True, blank = True)
	website_urls = models.CharField(max_length = 200, null = True, blank = True)
	github_urls = models.CharField(max_length = 200, null = True, blank = True)
	twitter_urls = models.CharField(max_length = 200, null = True, blank = True)
	facebook_urls = models.CharField(max_length = 200, null = True, blank = True)



	def __str__(self):
		return str(self.user)

class Post(models.Model):
	title = models.CharField(max_length=200)
	snippet = models.CharField(max_length=300,null= True, blank=True)
	header_image = models.ImageField(null = True,blank = True, upload_to = 'images/')
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