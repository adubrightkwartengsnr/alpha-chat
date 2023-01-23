from django.urls import path
from . import views


urlpatterns = [
     path('',views.home,name="home"),
     path('<int:tweet_id>',views.detail_page,name='detail'),
     path('tweet_view',views.tweets_view,name='tweet_view'),
     path('create_tweet',views.tweet_create_view, name = 'create_tweet')
     
]

