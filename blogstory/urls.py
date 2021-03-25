from django.urls import path
from . import views

app_name = 'blogstory'
urlpatterns = [
    path('<slug:story_slug>/', views.blogstory, name='blogstory'),
]