from django.shortcuts import get_object_or_404, render
from .models import AccountStory

def accountstory(request, story_slug):
  try:
    story = AccountStory.objects.get(slug=story_slug)
  except AccountStory.DoesNotExist:
    raise Http404("Story does not exist")
    print(story.is_ad)
  return render(request, 'accountstory/index.html', { 'story': story })
  
