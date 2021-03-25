from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogstory.models import BlogStory
from notifications.models import Notification
from userstory.models import UserStory, ReaderStory
from .models import Blog
from ads.models import Ad
from feed.models import Discover, Topten, Celebrity, Weview, Video, Finance, Future, Product, Productotd

class BlogListView(ListView):

    model = Blog
    template_name = 'blog/post.html'
    ordering = ['-pk']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = BlogStory.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['notification'] = 0
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).count()
        return context
        
class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blog/postdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = story = BlogStory.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['ad'] = Ad.objects.order_by('-pk')[:1]
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
