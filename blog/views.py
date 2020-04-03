from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator
# Create your views here.


def hello_world(request):
    return HttpResponse("hello, world")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.article_title
    breif = article.article_content
    detail = article.article_detail
    _id = article.article_id
    publish_date = article.publish_date

    return_str = "title: {}, brief: {}, detail: {}, id: {}, publish_date: {}".format(
        title, breif, detail, _id, publish_date
    )
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    all_article = Article.objects.all()
    top5_article_list=Article.objects.order_by('-publish_date')[:5]
    paginator = Paginator(all_article, 3)
    page_number = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page -1
    else:
        previous_page = page

    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_number + 1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'top5_article_list': top5_article_list
    })


def get_detail_page(request, article_id):
    all_articles = Article.objects.all()
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_articles):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_articles) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            current_article = article
            previous_article = all_articles[previous_index]
            next_article = all_articles[next_index]
            break

    section_list = current_article.article_detail.split("\n")
    return render(request, 'blog/detail.html', {
        'current_article': current_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article
    })
