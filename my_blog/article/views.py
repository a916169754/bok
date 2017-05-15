#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
top = Article.objects.all().order_by("-id")[0:3]
def home(request):
    posts = Article.objects.all().order_by("-date_time")
    paginator = Paginator(posts, 5) 
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list, 'top1' :top[0], 'top2' :top[1], 'top3' :top[2]})
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    
    return render(request, 'post.html', {'post' : post, 'top1' :top[0], 'top2' :top[1], 'top3' :top[2]})


def archives(request) :
    try:
        post_list = Article.objects.filter(date_time__year="2016",date_time__month="12").order_by("-date_time")
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False, 'top1' :top[0], 'top2' :top[1], 'top3' :top[2]})
def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')


def contos(request, cry):
    post_list = Article.objects.filter(category = cry)
    titles = []
    for post in post_list:
	if not(post.tag in titles):
	    titles.append(post.tag)
    return render(request, 'ContOS.html',{'post_list' :post_list, 'titles' :titles, 'top1' :top[0], 'top2' :top[1], 'top3' :top[2]})