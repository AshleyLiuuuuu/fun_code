# Create your models here.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('发布时间')
    last_edit_date = models.DateTimeField('最后修改时间')
