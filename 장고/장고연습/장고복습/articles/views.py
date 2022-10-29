
from django.shortcuts import redirect, render

import articles


from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by('-pk')
    # Template에 전달한다. 
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
def new(request):
    article_form = ArticleForm()
    context={
        'article_form': article_form

    }


    return render(request, 'articles/new.html',context=context)

def create(request):
    if request.user.is_authenticated:
        if request.method =='POST': 
            article_form = ArticleForm(request.POST, request.FILES)
            if article_form.is_valid():
                article_form.save()
                return redirect ('articles:index')
        else:
            article_form =ArticleForm()
        context={
        'article_form': article_form
        }
        return render(request, 'articles/new.html',context=context)
    else: return redirect('accounts:login')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)

    else:    
        article_form = ArticleForm(instance=article)
    context ={
        'article_form' : article_form
    }
    return render(request, 'articles/update.html', context)
