# Create your views here.
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import url
from django.urls import reverse
from django.views import generic

from .models import Article, Page, Tag, Category


class IndexView(generic.ListView):
    template_name = 'j4blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')  # [:5]


# class ArticleView(generic.DetailView):
#     template_name = 'j4blog/article.html'
#     model = Article
def article_detail(request, article_path):
    article = get_object_or_404(Article, path=article_path)
    return render(request, 'j4blog/article.html', {'article': article})


# class PageView(generic.DetailView):
#     template_name = 'j4blog/page.html'
#     model = Page
def page_detail(request, page_path):
    page = get_object_or_404(Page, path=page_path)
    return render(request, 'j4blog/page.html', {'page': page})


# class TagView(generic.DetailView):
#     template_name = 'j4blog/tag.html'
#     model = Tag
def tag_detail_and_list(request, tag_path):
    tag = get_object_or_404(Tag, path=tag_path)
    return render(request, 'j4blog/tag.html', {'tag': tag})

def category_detail_and_list(request, category_path):
    category = get_object_or_404(Category, path=category_path)
    return render(request, 'j4blog/category.html', {'category': category})
