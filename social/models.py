from django.db import models

class Post(models.Model):
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField()
  is_ad = models.BooleanField(default=False)
  ad_url = models.CharField(max_length=200, null=True)
  ad_cta = models.CharField(max_length=200, null=True)
  
  def __str__(self):
    return self.headline