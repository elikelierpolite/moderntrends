from django.db import models

class Funnel(models.Model):
  slug = models.SlugField(unique=True)
  headline = models.CharField(null=True,max_length=200)
  img = models.TextField()
  models.SlugField(unique=True)
  hook = models.CharField(null=True,max_length=200)
  theme = models.CharField(null=True,max_length=200)
  cta = models.CharField(null=True,max_length=200)
  url = models.TextField()
  p_img = models.TextField()
  description_title = models.CharField(null=True,max_length=200)
  description = models.TextField()
  body = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return self.headline