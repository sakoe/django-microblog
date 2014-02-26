from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
	title = models.CharField(max_length=128)
	text = RichTextField(config_name='spectacular_ckeditor')
	author = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, null=True,
                                   related_name='categories')

    def __unicode__(self):
        return self.name