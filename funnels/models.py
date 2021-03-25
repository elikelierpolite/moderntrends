from django.db import models
from ckeditor.fields import RichTextField

class Funnel(models.Model):
  headline = models.CharField(null=True,max_length=200)
  img = models.TextField()
  theme = models.CharField(null=True,max_length=200)
  cta = models.CharField(null=True,max_length=200)
  url = models.TextField()
  p_img = models.TextField()
  description_title = models.CharField(null=True,max_length=200)
  description = models.TextField()
  body = RichTextField(null=True, blank=True)
  
  def __str__(self):
    return self.headline