from django.contrib import admin

# Register your models here.

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['last_edit_date']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #inlines = [ChoiceInline]
    #list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    #search_fields = ['question_text']


admin.site.register(Article)
