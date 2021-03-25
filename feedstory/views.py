from django.shortcuts import get_object_or_404, render
from .models import Story, Page 
from feed.models import Topten

def feedstory(request, story_slug):
  try:
    story = Story.objects.get(slug=story_slug)
  except Story.DoesNotExist:
    raise Http404("Story does not exist")
  return render(request, 'feedstory/index.html', { 'story': story, })
  
