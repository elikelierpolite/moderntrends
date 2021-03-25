from django.shortcuts import get_object_or_404, render
from .models import BlogStory

def blogstory(request, story_slug):
  try:
    story = BlogStory.objects.get(slug=story_slug)
  except Story.DoesNotExist:
    raise Http404("Story does not exist")
    print(story.is_ad)
  return render(request, 'blogstory/index.html', { 'story': story })
  
