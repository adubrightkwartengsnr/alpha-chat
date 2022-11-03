from django.shortcuts import render
from django.http import Http404, HttpResponse,JsonResponse

from .models import Tweet

# Create your views here.

def home(request,*args,**kwargs):
    return HttpResponse("Hello World")

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