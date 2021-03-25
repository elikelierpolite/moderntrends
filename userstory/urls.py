from django.urls import path
from . import views

app_name = 'userstory'
urlpatterns = [
    path('<slug:story_slug>/', views.userstory, name='userstory'),
    path('reader/<slug:story_slug>/', views.readerstory, name='readerstory'),
]