from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test


def article_list(request):
    articles = Article.objects.all().order_by('date')
    common_tags = Article.tags.most_common()[:4]
    return render(request,'articles/article_list.html',{'articles':articles,'common_tags':common_tags})

def TagIndexView(request,slug):
    articles = Article.objects.filter(tags__slug=slug)
    common_tags = Article.tags.most_common()[:4]
    return render(request,'articles/article_list.html',{'articles':articles,'common_tags':common_tags})

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        sameName = False
        if form.is_valid():
            articles = Article.objects.all()
            for article in articles:
                if article.title == form.cleaned_data['title']:
                    sameName=True
                    return render(request,'articles/article_create.html',{'form':form,'sameName':sameName})
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})

@user_passes_test(lambda u: u.is_superuser)
def article_delete(request,slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return article_list(request)

@user_passes_test(lambda u: u.is_superuser)
def article_edit(request,slug):
    if request.method == 'POST':
        form = forms.EditArticle(request.POST,request.FILES)
        if form.is_valid():
            article = Article.objects.get(slug=slug)
            instance = form.save(commit=False)
            instance.author=article.author
            article.delete()
            instance.save()
            return redirect('articles:list')
    else:
        article = Article.objects.get(slug=slug)
        form = forms.EditArticle(initial={'title':article.title,'body':article.body,'slug':article.slug,'thumb':article.thumb,'tags':article.tags.all()})
        form.title=article.title
        form.body = article.body
        form.thumb = article.thumb
        form.tags = article.tags

    return render(request,'articles/article_edit.html',{'form':form,'slug':slug})
