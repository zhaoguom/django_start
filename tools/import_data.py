#!/usr/bin/python
# -*-encoding=utf8 -*-

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_start.settings')
django.setup()

from blog.models import Article

data_path = '../data/article'


if __name__ == "__main__":
    article = Article()
    with open("c:/users/zhaoguo.ma/desktop/1.txt", encoding="utf8") as f:
        article.article_title = f.readline()
        article.article_content = f.readline()
        article.article_detail = f.read()
        article.save()
