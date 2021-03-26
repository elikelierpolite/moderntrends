from django.urls import path
from .views import funnelpage

app_name = 'funnels'
urlpatterns = [
    path('<slug:funnel>/', funnelpage, name='funneldetail'),
]
