from django.contrib import admin

# Register your models here.

from .models import Article, Comment, Flag, Category


# class ArticleAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['title']}),
#         ('test', {'fields': ['pub_date']}),
#     ]
#     #inlines = [CommentInline]
#     list_display = ('title', 'pub_date', 'last_edit_date')
#     list_filter = ['pub_date']
#     search_fields = ['content','title']


#admin.site.register(Article, ArticleAdmin)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Flag)
admin.site.register(Category)
#
