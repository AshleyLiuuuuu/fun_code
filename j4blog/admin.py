from django.contrib import admin

from .models import Article, Comment, Tag, Category, Page


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
     list_display = ('title', 'pub_date', 'path', 'is_published')


admin.site.register(Article, ArticleAdmin)
#admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Page)
