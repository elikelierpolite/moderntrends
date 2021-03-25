from django.shortcuts import get_object_or_404, render
from .models import UserStory, ReaderStory

def userstory(request, story_slug):
  try:
    story = UserStory.objects.get(slug=story_slug)
  except UserStory.DoesNotExist:
    raise Http404("Story does not exist")
  return render(request, 'userstory/index.html', { 'story': story })
  
def readerstory(request, story_slug):
  try:
    story = ReaderStory.objects.get(slug=story_slug)
  except ReaderStory.DoesNotExist:
    raise Http404("Story does not exist")
  return render(request, 'userstory/index.html', { 'story': story })
  
