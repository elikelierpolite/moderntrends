from django.urls import path
from . import views

app_name = 'accountstory'
urlpatterns = [
    path('<slug:story_slug>/', views.accountstory, name='accountstory'),
]