from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_header', 'article_id', 
                    'publication_date', 'get_tags')


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
