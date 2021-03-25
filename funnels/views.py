from django.shortcuts import get_object_or_404, render
from .models import Funnel

def funnelpage(request, funnel):
  try:
    landing_page = Funnel.objects.filter(pk=funnel)
  except Funnel.DoesNotExist:
    raise Http404("funmel does not exist")
  return render(request, 'funnels/funnel.html', { 'landing_page': landing_page })