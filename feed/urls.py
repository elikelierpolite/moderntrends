from django.urls import path
from .views import ArticleListView, ArticleDetailView, News, NewsListView, SportsListView, HealthListView, PoliticsListView, BusinessListView, Weather, DiscoverListView, DiscoverDetailView, TenListView, ListDetailView, CelebListView, CelebDetailView, WeViewList, WeViewDetailView, VideoListView, VideoDetailView, FinanceListView, FinanceDetailView, FutureListView, FutureDetailView, ProductListView, ProductDetailView

app_name = 'articles'
urlpatterns = [
    #path('', views.feed, name='feed')
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('news/', News, name='news'),
    path('breakingnews/', NewsListView.as_view(), name='breakingnews'),
    path('sports/', SportsListView.as_view(), name='sports'),
    path('health/', HealthListView.as_view(), name='health'),
    path('politics/', PoliticsListView.as_view(), name='politics'),
    path('business/', BusinessListView.as_view(), name='business'),
    path('weather/', Weather, name='weather'),
    path('discover/', DiscoverListView.as_view(), name='discover'),
    path('discover/<slug:slug_text>/', DiscoverDetailView, name='discoverdetail'),
    path('ten/', TenListView.as_view(), name='topten'),
    path('ten/<slug:slug>/', ListDetailView.as_view(), name='listdetail'),
    path('celebrities/', CelebListView.as_view(), name='celebrities'),
    path('celebrities/<slug:slug>/', CelebDetailView.as_view(), name='celebdetail'),
    path('weview/', WeViewList.as_view(), name='weview'),
    path('weview/<slug:slug>/', WeViewDetailView.as_view(), name='weviewdetail'),
    path('video/', VideoListView.as_view(), name='video'),
    path('video/<slug:slug>/', VideoDetailView.as_view(), name='videodetail'),
    path('finance/', FinanceListView.as_view(), name='finance'),
    path('finance/<slug:slug>/', FinanceDetailView.as_view(), name='financedetail'),
    path('future/', FutureListView.as_view(), name='future'),
    path('future/<slug:slug>/', FutureDetailView.as_view(), name='futuredetail'),
    path('shopping/', ProductListView.as_view(), name='shopping'),
    path('shopping/<slug:slug>/', ProductDetailView.as_view(), name='productdetail'),

]
