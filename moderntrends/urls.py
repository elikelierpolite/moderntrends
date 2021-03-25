"""moderntrends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from feed.sitemaps import ArticleSitemap, BlogSitemap
from feed import views as article_views
from feed import views as blog_views

sitemaps = {
  'articles': ArticleSitemap,
  'posts': BlogSitemap
}

urlpatterns = [
    path('', include('feed.urls')),
    path('feedstory/', include('feedstory.urls')),
    path('blogstory/', include('blogstory.urls')),
    path('accountstory/', include('accountstory.urls')),
    path('userstory/', include('userstory.urls')),
    path('ads/', include('ads.urls')),
    path('blog/', include('blog.urls')),
    path('social/', include('social.urls')),
    path('preview/', include('funnels.urls')),
    path('admin/', admin.site.urls),
    path('articles/<slug:article_slug>', article_views.article, name='articles'),
    path('posts/<slug:post_slug>', blog_views.blog, name='posts'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('robots.txt', include('robots.urls')),
    path('account/', include('accounts.urls')),
    path('subscribe/', include('subscribers.urls'))
]
