from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.TextField()
	date_published = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'{self.title} ||| {self.author}'
