from django.db import models
from django.urls import reverse

class Blog(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  hook = models.TextField(null=True)
  description = models.CharField(max_length=200, null=True)
  body = models.TextField(blank=True, null=True)
  
  def get_absolute_url(self):
    return reverse('posts', args=[str(self.slug)])
  
  def __str__(self):
    return self.headline