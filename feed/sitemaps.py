from django.contrib.sitemaps import Sitemap
from .models import Article, Topten
from blog.models import Blog

class ArticleSitemap(Sitemap):
  def items(self):
    return Article.objects.all()
    
class BlogSitemap(Sitemap):
  def items(self):
    return Blog.objects.all()
    