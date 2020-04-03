from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.TextField()
    article_content = models.TextField()
    article_detail = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_title