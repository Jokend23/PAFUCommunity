from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import *


class ArticleAdminField(admin.ModelAdmin):
    list_display = ('article_title', 'article_create_date', 'article_published_date')


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('__all__')


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')
    search_fields = ['__str__']


class ArticleStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')
    search_fields = ['__str__']

class NewsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'news_create_date', 'news_published_date', 'news_author')
    search_fields = ['__str__']

admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(ArticleStatistic, ArticleStatisticAdmin)
admin.site.register(UploadedFile)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Contact)
admin.site.register(About, ArticleAdmin)
