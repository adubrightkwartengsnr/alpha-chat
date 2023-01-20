import random
from django.shortcuts import render
from django.template import loader
from django.http import Http404, HttpResponse,JsonResponse

from .models import Tweet

# Create your views here.

def home(request,*args,**kwargs):
    context = {
        
    }
    return render(request,"tweets/home.html",context = context,status=200)

def tweets_view(request,*args,**kwargs):
    """"
    REST API TO BE CONSUMED BY THE FRONTEND
    """
    query_set = Tweet.objects.all()
    tweet_list = [{'id':tweet.id, 'content':tweet.content,'likes':random.randint(0,100) } for tweet in query_set]
    data = {
        'isUser':False,
        'response':tweet_list
    }
    return JsonResponse(data)

def detail_page(request,tweet_id,*args,**kwargs):
# REST API VIEW FOR THE CONTENT
    data = {
            "id" : tweet_id
    }
    status = 200
    try:
        obj= Tweet.objects.get(id = tweet_id)
        data["content"] = obj.content
        # data['image'] = obj.image.url
    except:
        data["message"] = "Not Found"
        status = 404

    
    return JsonResponse(data,status=status)