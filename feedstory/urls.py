from django.urls import path
from . import views

app_name = 'feedstory'
urlpatterns = [
    path('<slug:story_slug>/', views.feedstory, name='feedstory'),
]