from django.contrib import admin
from .models import NewsArticle

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'source_id',
        'source_name',
        'author',
        'title',
        'description',
        'url_to_image',
        'published_at',
        'content',
    )

admin.site.register(NewsArticle, NewsArticleAdmin)
