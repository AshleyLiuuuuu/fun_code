# Create your models here.
from django.db import models


class Article(models.Model):
    article_title = models.CharField(verbose_name='标题', max_length=200)
    article_content = models.TextField(verbose_name='文章内容')
    pub_date = models.DateTimeField(verbose_name='发布时间', auto_now=True)
    last_edit_date = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    # id =models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(verbose_name='标签', max_length=20)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#
#
# class Comment(models.Model):
#     comment_content = models.TextField(verbose_name='评论')
#
#     # article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.content[:20]
#
#
# class Category(models.Model):
#     category_name = models.CharField(verbose_name='分类', max_length=20)
#
#     def __str__(self):
#         return self.name
