from django.urls import path

from .views import article_list, home

urlpatterns = [
    path('', home, name="home"),  # Endpoint dla '/'
    path('articles/', article_list, name='article_list'),
]
