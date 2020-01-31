from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Sum, Q
from django.contrib import auth
from django.views import View
from django.core.mail import *

from .filter import *
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


def articles_list(request):
    articles = Article.objects.filter(article_published_date__lte=timezone.now()).order_by('-article_published_date')
    news = News.objects.filter(is_published__exact=True).order_by('-news_published_date')[:4]
    menus = Article.objects.all()
    game_articles = Article.objects.filter(article_type__exact=1).order_by('-article_published_date')
    filter = ArticleFilter(request.GET, queryset=Article.objects.all().order_by('-article_published_date'))
    titlefilter = ArticleTitleFilter(request.GET, queryset=Article.objects.all().order_by('-article_type'))

    content = {
        'menu': menus,
        'news':news,
        'articles': articles,
        'game_articles': game_articles,
        'filter': filter,
        'titlefilter': titlefilter,
    }

    return render(request, 'article_list.html', content)

def news_list(request):
    list = News.objects.filter(is_published__exact=True).order_by('-news_published_date')

    content = {
        'list':list,
    }

    return render(request, 'news_list.html', content)

def game_articles_list(request):
    type = Article.objects.filter(article_type__type='Игровая тематика')
    date = type.exclude(article_published_date__lte=timezone.now()).order_by('-article_published_date')

    content = {
        'game_articles': date
    }

    return render(request, 'game_list.html', content)


def index_menu(request):
    menus = Article.objects.filter(article_published_date__lte=timezone.now()).order_by('-article_published_date')

    return render(request, 'menu_list.html', {'menus': menus})


def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_author = request.user
            article.article_published_date = timezone.now()
            article.article_create_date = timezone.now()
            article.save()
            return redirect('article-detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article_new.html', {'form': form})


def article_detail(request, pk):
    article_detail = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article_detail': article_detail})

def news_detail(request, pk):
    news_detail = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news_detail': news_detail})

def about_list(request):
    about_list = get_object_or_404(About)
    return render(request, 'about_list.html', {'about_list': about_list})


def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['0jokend0@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, '0jokend0@gmail.com', recepients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact.html', {'form': form, 'username': auth.get_user(reguest).username})


def thanks(request):
    thanks = 'thanks'
    return render(request, 'thanks.html', {'thanks': thanks})

def searchresultview(request):

    query = request.GET.get('q')
    object_list = Article.objects.filter(Q(article_title__icontains=query)).order_by('?')[:10]
    return render(request, 'search_list.html', {'object_list':object_list})


class EArticleView(View):
    template_name = 'article_list.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs['article_id'])

        context = {}

        obj, created = ArticleStatistic.objects.get_or_create(
            defaults={
                "article": article,
                "date": timezone.now()

            },
            date=timezone.now(), article=article)
        obj.views += 1
        obj.save(update_fields=['views'])
        popular = ArticleStatistic.objects.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
        ).values(
            'article_id', 'article__title'
        ).annotate(
            views=Sum('views')
        ).order_by('-views')[:5]
        context['popular_list'] = popular

        return render(template_name=self.template_name, context=context)
