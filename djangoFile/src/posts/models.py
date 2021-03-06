from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save 
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class PostManager(models.Model):
	def active(self, *args, **kwargs):

		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
	# filebase, extension = filename,split(".")
	return "%s/%s" %(instance.id,filename)
class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location,
			null=True,blank=True, height_field='height_field',
			width_field='width_field' )
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=0)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


	objects = PostManager()
	def __unicode__(self):
		return self.title
		
	def get_absolut_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["-timestamp","-updated"]

	def get_edit_url(self):
		return reverse("posts:update", kwargs={"id": self.id})

	def get_delete_url(self):
		return reverse("posts:delete", kwargs={"id": self.id})

	class Meta:
		ordering = ["-timestamp","-updated"]


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender,instance, *args, **kwargs):
	slug = slugify(instance.title)
	exists = Post.objects.filter(slug=slug).exists()
	if exists:
		slug = "%s-%s" %(slug, instance.id)
	instance.slug = slug

pre_save.connect(pre_save_post_receiver, sender=Post)
