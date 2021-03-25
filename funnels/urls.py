from django.urls import path
from .views import funnelpage

app_name = 'funnels'
urlpatterns = [
    path('<int:funnel>/', funnelpage, name='funneldetail'),
]
