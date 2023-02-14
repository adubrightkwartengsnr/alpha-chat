import random
from django.shortcuts import render,redirect
from django.template import loader
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from .models import Tweet
from .forms import TweetForm


# Create your views here.

def home(request, *args, **kwargs):
    context = {

    }
    return render(request, "tweets/home.html", context=context, status=200)


def tweets_view(request, *args, **kwargs):
    """"
    REST API TO BE CONSUMED BY THE FRONTEND
    """
    query_set = Tweet.objects.all()
    tweet_list = [{'id': tweet.id, 'content': tweet.content, 'likes': random.randint(0, 100)} for tweet in query_set]
    data = {
        'isUser': False,
        'response': tweet_list
    }
    return JsonResponse(data)


def detail_page(request, tweet_id, *args, **kwargs):

    #REST  API VIEW FOR THE CONTENT
    # Return json data
    # Consume by Javascript
    data = {
        "id": tweet_id
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
        # data['image'] = obj.image.url
    except:
        data["message"] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)

ALLOWED_HOSTS =settings.ALLOWED_HOSTS
def tweet_create_view(request,*args,**kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    print('next_url',next_url)
    if form.is_valid():
        obj =form.save(commit=False)
        obj.save()
        if next_url != None and url_has_allowed_host_and_scheme(next_url,ALLOWED_HOSTS,require_https=True):
            return redirect(next_url)
        form = TweetForm()
    return render(request,'components/form.html',context = {'form':form})
