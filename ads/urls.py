from django.urls import path
from ads import views

app_name = 'ads'
urlpatterns = [
    path('<slug:ad_slug>/', views.ad, name='ad'),
]