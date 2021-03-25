from django.db import models

class BlogStory(models.Model):
  story_text = models.CharField(null=True,max_length=200)
  story_img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  is_ad = models.BooleanField()
  ad_url = models.TextField(null=True, blank=True)
  ad_cta = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.story_text


class BlogPage(models.Model):
  story= models.ForeignKey(BlogStory, on_delete=models.CASCADE)
  story_title = models.CharField(max_length=200, null=True)
  story_img = models.TextField(null=True)
  up_next_title = models.CharField(max_length=200, null=True)
  up_next_img = models.TextField(null=True)
  up_next_url = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.story_title