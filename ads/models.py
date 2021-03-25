from django.db import models

class Ad(models.Model):
    ad_headline = models.CharField(null=True,max_length=200)
    ad_img = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    ad_theme = models.CharField(null=True,max_length=200)
    ad_hook = models.CharField(null=True,max_length=200)
    ad_cta = models.CharField(null=True,max_length=200)
    ad_url = models.TextField(null=True)
    
    def __str__(self):
        return self.ad_headline

