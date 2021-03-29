from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from feedstory.models import Story
from blog.models import Blog
from notifications.models import Notification
from subscribers.models import Subscriber
from userstory.models import UserStory, ReaderStory
from ads.models import Ad
from .models import Article, Discover, Topten, Celebrity, Weview, Video, Finance, Future, Product, Productotd

import urllib.request
import json

#!!************* SITEMAPS ***************!#
def article(request, article_slug):
  item = get_object_or_404(Article, slug=article_slug)
  ad = Ad.objects.order_by('-pk')[:1]
  story = Story.objects.order_by('-pk')
  userstory = UserStory.objects.order_by('-pk')
  readerstory = ReaderStory.objects.order_by('-pk')
  discover = Discover.objects.order_by('-pk')[0:1]
  topten = Topten.objects.order_by('-pk')[:1]
  celebrity = Celebrity.objects.order_by('-pk')[:1]
  weview = Weview.objects.order_by('-pk')[:1]
  video = Video.objects.order_by('-pk')[:1]
  finance = Finance.objects.order_by('-pk')[:1]
  future = Future.objects.order_by('-pk')[:1]
  product = Product.objects.order_by('-pk')[:1]
  return render (request, 'feed/articles.html', {'article':item, 'ad':ad, 'story':story, 'userstory':userstory, 'readerstory':readerstory, 'discover':discover, 'topten':topten, 'celebrity':celebrity, 'weview':weview, 'video':video, 'finance':finance, 'future':future, 'product':product})
  
def blog(request, post_slug):
  item = get_object_or_404(Blog, slug=post_slug)
  ad = Ad.objects.order_by('-pk')[:1]
  story = Story.objects.order_by('-pk')
  userstory = UserStory.objects.order_by('-pk')
  readerstory = ReaderStory.objects.order_by('-pk')
  discover = Discover.objects.order_by('-pk')[0:1]
  topten = Topten.objects.order_by('-pk')[:1]
  celebrity = Celebrity.objects.order_by('-pk')[:1]
  weview = Weview.objects.order_by('-pk')[:1]
  video = Video.objects.order_by('-pk')[:1]
  finance = Finance.objects.order_by('-pk')[:1]
  future = Future.objects.order_by('-pk')[:1]
  product = Product.objects.order_by('-pk')[:1]
  return render (request, 'blog/blog.html', {'blog':item, 'ad':ad, 'story':story, 'userstory':userstory, 'readerstory':readerstory, 'discover':discover, 'topten':topten, 'celebrity':celebrity, 'weview':weview, 'video':video, 'finance':finance, 'future':future, 'product':product})
  
#!!************* SITEMAPS *************!!#

class ArticleListView(ListView):

    model = Article
    template_name = 'feed/index.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request == 'POST':
          email = self.request.POST['form5Example2']
          email = Subscriber.objects.create_subscriber(email=email)
          email.save()
          return redirect(self.request, 'feed/index.html')
          print("subscribed")
        else:
          context['ad'] = Ad.objects.order_by('-pk')
          context['story'] = Story.objects.order_by('-pk')
          context['userstory'] = UserStory.objects.order_by('-pk')
          context['readerstory'] = ReaderStory.objects.order_by('-pk')
          context['notification'] = 0
          if self.request.user.is_authenticated:
            context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
          return context
  
  
class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')[:1]
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context

def News(request):
  story = Story.objects.order_by('-pk')
  ad = Ad.objects.order_by('-pk')
  userstory = UserStory.objects.order_by('-pk')
  readerstory = ReaderStory.objects.order_by('-pk')
  notification = 0
  if request.user.is_authenticated:
    notification = Notification.objects.filter(to=request.user, seen=False).count()
  context = {'ad':ad, 'story':story, 'userstory':userstory, 'readerstory':readerstory, 'notification':notification}
  return render(request, 'feed/news.html', context)
  
class NewsListView(ListView):

    model = Article
    template_name = 'feed/breakingnews.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class SportsListView(ListView):

    model = Article
    template_name = 'feed/sports.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class HealthListView(ListView):

    model = Article
    template_name = 'feed/health.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class PoliticsListView(ListView):

    model = Article
    template_name = 'feed/politics.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class BusinessListView(ListView):

    model = Article
    template_name = 'feed/business.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
def Weather(request):
  story = Story.objects.order_by('-pk')
  ad = Ad.objects.order_by('-pk')
  userstory = UserStory.objects.order_by('-pk')
  readerstory = ReaderStory.objects.order_by('-pk')
  notification = 0
  if request.user.is_authenticated:
    notification = Notification.objects.filter(to=request.user, seen=False).count()
  context = {'ad':ad, 'story':story, 'userstory':userstory, 'readerstory':readerstory, 'notification':notification}
  if request.method == 'POST':
      city = request.POST['city']

      source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=9bb1dab5788a64a1cdf4404353ba86d3').read()
      list_of_data = json.loads(source)

      data = {
          "country_code": str(list_of_data['sys']['country']),
          "coordinate": str(list_of_data['coord']['lon']) + ', '
          + str(list_of_data['coord']['lat']),

          "temp": str(list_of_data['main']['temp']) + ' °C',
          "pressure": str(list_of_data['main']['pressure']),
          "humidity": str(list_of_data['main']['humidity']),
          'main': str(list_of_data['weather'][0]['main']),
          'description': str(list_of_data['weather'][0]['description']),
          'icon': list_of_data['weather'][0]['icon'],
          'ad':ad, 'story':story, 'userstory':userstory, 'readerstory':readerstory, 'notification':notification
      }
      print(data)
  else:
      data = {'ad':ad, 'story':story, 'userstory':userstory, 'readerstory':readerstory, 'notification':notification}
  return render(request, "feed/weather.html", data)
  
  
class DiscoverListView(ListView):

    model = Discover
    template_name = 'feed/discover.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
  
def DiscoverDetailView(request, slug_text):
  try:
    discover = Discover.objects.get(slug=slug_text)
  except Story.DoesNotExist:
    raise Http404("Discover does not exist")
  return render(request, 'feed/discoverdetail.html', { 'discover': discover })
  
class TenListView(ListView):

    model = Topten
    template_name = 'feed/topten.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
  
class ListDetailView(DetailView):

    model = Topten
    template_name = 'feed/listdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')[1:2]
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class CelebListView(ListView):

    model = Celebrity
    template_name = 'feed/celebrities.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class CelebDetailView(DetailView):

    model = Celebrity
    template_name = 'feed/celebdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')[2:3]
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class WeViewList(ListView):

    model = Weview
    template_name = 'feed/weview.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class WeViewDetailView(DetailView):

    model = Weview
    template_name = 'feed/weviewdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class VideoListView(ListView):

    model = Video
    template_name = 'feed/video.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class VideoDetailView(DetailView):

    model = Video
    template_name = 'feed/videodetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class FinanceListView(ListView):

    model = Finance
    template_name = 'feed/finance.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class FinanceDetailView(DetailView):

    model = Finance
    template_name = 'feed/financedetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['ad'] = Ad.objects.order_by('-pk')[4:5]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class FutureListView(ListView):

    model = Future
    template_name = 'feed/future.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class FutureDetailView(DetailView):

    model = Future
    template_name = 'feed/futuredetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')[3:4]
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class ProductListView(ListView):

    model = Product
    template_name = 'feed/product.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.order_by('-pk')
        context['story'] = story = Story.objects.order_by('-pk')
        context['potd'] = Productotd.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class ProductDetailView(DetailView):

    model = Product
    template_name = 'feed/productdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = Story.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['discover'] = Discover.objects.order_by('-pk')[0:1]
        context['topten'] = Topten.objects.order_by('-pk')[:1]
        context['celebrity'] = Celebrity.objects.order_by('-pk')[:1]
        context['weview'] = Weview.objects.order_by('-pk')[:1]
        context['video'] = Video.objects.order_by('-pk')[:1]
        context['finance'] = Finance.objects.order_by('-pk')[:1]
        context['future'] = Future.objects.order_by('-pk')[:1]
        context['product'] = Product.objects.order_by('-pk')[:1]
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context