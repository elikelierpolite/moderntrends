from django.shortcuts import get_object_or_404, render
from .models import Ad

def ad(request, ad):
  try:
    ad = Ad.objects.get(slug=ad_slug)
  except Story.DoesNotExist:
    raise Http404("ad does not exist")
  return render(request, 'ads/index.html', { 'ad': ad })