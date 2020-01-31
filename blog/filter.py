import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):

    class Meta:
        model = Article
        fields = ['article_type']

class ArticleTitleFilter(django_filters.FilterSet):

    article_title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Article
        fields = ['article_title']