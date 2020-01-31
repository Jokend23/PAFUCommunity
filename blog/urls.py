from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/search', views.searchresultview, name='search_results'),
    path('contact/', views.contactform, name='contact'),
    path('contact/thanks/', views.thanks, name='thanks'),
    path('about/', views.about_list, name='about'),
    path('', views.articles_list, name='articles_list'),
    path('game/', views.game_articles_list, name='game_article_list'),
    path('catalog/', views.index_menu, name='menu_list'),
    path('article/<int:pk>', views.article_detail, name='article-detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>', views.news_detail, name = 'news_detail'),
    path('article/new/', views.article_new, name='article_new'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
