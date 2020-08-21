# Create your models here.
from django.contrib.auth.models import User
from django.db import models, IntegrityError
from django.utils import timezone


# 分类
class Category(models.Model):
    name = models.CharField(verbose_name='分类', max_length=100, unique=True)
    description = models.TextField(verbose_name='描述', blank=True)
    path = models.CharField(verbose_name='路径', blank=True, null=True, max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:  # 项目首次保存时
            if not self.path:  # 用标题填写URL
                try:
                    Category.objects.get(path=self.name)  # 已存在当前标题的URL
                    self.path = self.name + '-' + str(timezone.now().timestamp())
                except Category.DoesNotExist:  # 确保唯一
                    self.path = self.name
        elif not self.path:  # 尝试修改URL为空时
            self.path = self.name + '-' + str(timezone.now().timestamp())

        super(Category, self).save(*args, **kwargs)


# 标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签', max_length=100, unique=True)
    description = models.TextField(verbose_name='描述', blank=True)
    path = models.CharField(verbose_name='URL', max_length=100, blank=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:  # 项目首次保存时
            if not self.path:  # 用标题填写URL
                try:
                    Tag.objects.get(path=self.name)  # 已存在当前标题的URL
                    self.path = self.name + '-' + str(timezone.now().timestamp())
                except Tag.DoesNotExist:  # 确保唯一
                    self.path = self.name
        elif not self.path:  # 尝试修改URL为空时
            self.path = self.name + '-' + str(timezone.now().timestamp())

        super(Tag, self).save(*args, **kwargs)


# 文章
class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='文章内容', blank=True)
    pub_date = models.DateTimeField(verbose_name='发布时间', blank=True, null=True)
    last_edit_date = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    path = models.CharField(verbose_name='自定义路径', max_length=100, unique=True, blank=True)
    draft = models.BooleanField(verbose_name='草稿', default=False)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # 一个分类可以对应多篇文章
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签与文章是多对多关系
    tag = models.ManyToManyField(Tag, blank=True, null=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title

    def is_published(self):
        if self.draft:
            return '草稿'
        if self.pub_date <= timezone.now():
            return '已发布'
        return '待发布'

    is_published.admin_order_field = 'pub_date'
    is_published.short_description = '发布状态'

    def save(self, *args, **kwargs):
        if not self.id:  # 项目首次保存时
            if not self.pub_date:  # 填写发布日期
                self.pub_date = timezone.now()
            if not self.path:  # 用标题填写URL
                try:
                    Article.objects.get(path=self.title)  # 已存在当前标题的URL
                    self.path = self.title + '-' + str(timezone.now().timestamp())
                except Article.DoesNotExist:  # 确保唯一
                    self.path = self.title
        elif not self.path:  # 尝试修改URL为空时
            self.path = self.title + '-' + str(timezone.now().timestamp())

        self.last_edit_date = timezone.now()

        super(Article, self).save(*args, **kwargs)


# 页面
class Page(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100, unique=True)
    content = models.TextField(verbose_name='页面内容', blank=True)
    pub_date = models.DateTimeField(verbose_name='发布时间')
    last_edit_date = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    path = models.CharField(verbose_name='自定义路径', max_length=100, blank=True, null=True, unique=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:  # 项目首次保存时
            if not self.pub_date:  # 填写发布日期
                self.pub_date = timezone.now()
            if not self.path:  # 用标题填写URL
                try:
                    Page.objects.get(path=self.title)  # 已存在当前标题的URL
                    self.path = self.title + '-' + str(timezone.now().timestamp())
                except Page.DoesNotExist:  # 确保唯一
                    self.path = self.title
        elif not self.path:  # 尝试修改URL为空时
            self.path = self.title + '-' + str(timezone.now().timestamp())

        self.last_edit_date = timezone.now()

        super(Page, self).save(*args, **kwargs)


# 评论
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    pub_date = models.DateTimeField(verbose_name='发布时间', auto_now=True)
    nickname = models.CharField(verbose_name='昵称', max_length=100)
    email = models.EmailField(verbose_name='E-mail', max_length=100, blank=True, null=True)
    domain = models.CharField(verbose_name='域名', max_length=100, blank=True, null=True)

    # 一篇文章或页面对应多个评论
    # article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True)
    # page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.content[:20]
