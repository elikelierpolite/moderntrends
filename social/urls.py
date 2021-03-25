from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('', views.home.as_view(), name='social-home')
]
