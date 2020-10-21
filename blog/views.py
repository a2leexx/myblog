from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect
import django.utils as utils

from django.core.paginator import Paginator
from .models import Article, Tag


def index(request):
    """ Возвращает ответ со списком опубликованных статей в блоге. """
    page_number = request.GET.get('page')
    articles = Article.published_articles.all()
    paginator = Paginator(articles, 2) # 10 страниц на страницу
    context = {'page' : paginator.get_page(page_number)} 
    return render(request, 'blog/index.html', context)


def show_article(request, article_id):
    """ Возвращает ответ со статьей с идентификатором article_id """
    try:
        article = Article.published_articles.get(article_id = article_id)
    except Article.DoesNotExist:
        raise Http404()
   
    html_text = article.html()
    context = {'html_text' : html_text, 'tags' : article.tags.all(), 
                'publication_date' : article.publication_date}
    
    return render(request, 'blog/article.html', context)


def view_articles_with_tag(request, tag_id):
    """ Возвращает статьи, помеченные тегом с идентификатором tag_id """
    page_number = request.GET.get('page')
    
    articles = Article.published_articles.filter(tags__tag_id = tag_id)
    paginator = Paginator(articles, 2)
    page = paginator.get_page(page_number)
    
    tag_name = Tag.objects.get(tag_id = tag_id).tag_name
    context = {'page' : page, 'tag_name' : tag_name} 
    return render(request, 'blog/tags.html', context)


def view_all_tags(request):
    """ Возвращает ответ со списком всех тегов, присутствующих на сайте """
    tags = Tag.objects.all()
    context = {'tags' : tags}
    return render(request, 'blog/alltags.html', context)


def search(request):
    """ Возвращает ответ со поисковый запрос по блогу """
    if request.method == 'GET':
        page_num = request.GET.get('page') # номер просматриваемой страницы
        search_str = request.GET.get('search') # искомая строка

        if search_str is None:
            search_str = ''

        # Сохраняем search_str в формате application/x-www-form-urlencoded. 
        # Это нужно для создания ссылок перехода на другие страницы.
        search_urlencoded = utils.http.urlencode({'search' : search_str}) 

        articles = Article.published_articles. \
            filter(markdown_text__icontains = search_str)
        paginator = Paginator(articles, 2)
        page = paginator.get_page(page_num)
        context = {'page' : page, 
                   'search_str' : search_str,
                   'search_urlencoded' : search_urlencoded}

        return render(request, 'blog/searchresult.html', context)
    

    
