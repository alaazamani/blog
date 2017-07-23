from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Recipe(models.Model):
	length = models.DurationField()
	content = models.TextField()
	picture = models.ImageField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title