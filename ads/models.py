from django.db import models
from ckeditor.fields import RichTextField

class Ad(models.Model):
  ad_headline = models.CharField(null=True,max_length=200)
  ad_img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  ad_theme = models.CharField(null=True,max_length=200)
  ad_hook = models.CharField(null=True,max_length=200)
  ad_cta = models.CharField(null=True,max_length=200)
  url = models.CharField(null=True,max_length=200)
    
  def __str__(self):
    return self.ad_headline
