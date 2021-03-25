from django.shortcuts import render
from accountstory.models import AccountStory
from django.views.generic.list import ListView
from .models import Post
from notifications.models import Notification
from userstory.models import UserStory, ReaderStory

class home(ListView):

    model = Post
    template_name = 'social/index.html'
    ordering = ['-pk']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = AccountStory.objects.order_by('-pk')
        context['userstory'] = UserStory.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        context['data'] = Notification.objects.order_by('-pk')
        context['readerstory'] = ReaderStory.objects.order_by('-pk')
        if self.request.user.is_authenticated:
          context['notification'] = Notification.objects.filter(to=self.request.user, seen=False).update(seen=True)
        return context
