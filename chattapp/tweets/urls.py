from django.urls import path
from . import views


urlpatterns = [
     path('',views.home,name="home"),
     path('<int:tweet_id>',views.detail_page,name='detail')
     
]

