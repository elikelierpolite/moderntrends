from django.db import models

class Post(models.Model):
  img = models.TextField()
  ad_url = models.CharField(max_length=200, null=True)
  ad_cta = models.CharField(max_length=200, null=True)