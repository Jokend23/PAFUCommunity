from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin


def rename_file(instance, filename):
    file_name = filename.split('.')[0]
    file_type = filename.split('.')[-1]
    return 'article_files/{0}.{1}'.format(file_name, file_type)


def rename_image(instance, filename):
    image_name = filename.split('.')[0]
    image_type = filename.split('.')[-1]
    return 'article_images/{0}.{1}'.format(image_name, image_type)


class UploadedFile(models.Model):
    file_name = models.CharField(max_length=100, verbose_name='Название файла')
    file = models.FileField(upload_to=rename_file, verbose_name='Прикрепленный файл')
    file_create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки файла')

    def __str__(self):
        return '{0} | {1}'.format(self.file_name, self.file_create_date)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class ArticleType(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тематика')
    slug = models.SlugField(verbose_name='Транслит', null=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

class Article(models.Model):
    article_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    article_title = models.CharField(max_length=100, verbose_name='Название')
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name='Тематика')
    article_text_short = models.TextField(verbose_name='Краткое содержание')
    article_text = models.TextField(verbose_name='Текст')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    article_create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    article_published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    article_image = models.ImageField(upload_to=rename_image, verbose_name='Изображение', blank=True, null=True)
    article_files = models.ManyToManyField(UploadedFile, verbose_name='Прикрепленный файлы', blank=True)

    def __str__(self):
        return '{0}  ||  {1}  ||  {2}'.format(self.article_title, self.article_create_date, self.article_published_date)

    def published(self):
        self.article_published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class ArticleStatistic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.article.article_title

    class Meta:
        verbose_name = 'Статистика Статьи'
        verbose_name_plural = 'Статистики статей'

class About(models.Model):
    title = models.CharField(max_length = 100, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to=rename_image, verbose_name='Изображение', blank=True, null=True)
    files = models.ManyToManyField(UploadedFile, verbose_name='Прикрепленный файлы', blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакт'

    def __str__(self):
        return self.title

class Contact(models.Model):
    subject = models.CharField(max_length=100, verbose_name ='Тема')
    sender = models.EmailField(verbose_name = 'E-mail')
    massage = models.TextField(verbose_name = 'Сообщение')
    copy = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return {0}  |  {1}.format(self.subject, self.sender)

class News(models.Model):
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    news_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    news_create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    news_published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    news_title = models.CharField(max_length=100, verbose_name='Название')
    news_text_short = models.TextField(verbose_name='Краткое содержание')
    news_text = models.TextField(verbose_name='Текст')
    news_image = models.ImageField(upload_to=rename_image, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.news_title
# Модель комментариев
# class Comment(models.Model):
#	path = ArrayField(models.IntegerField())
#	article_id = models.ForeignKey(Article, verbose_name ='ID статьи')
#	author_id = models.ForeignKey(User)
#	comment_text = models.TextField(verbose_name='Комментарий')
#	pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

#	class Meta:
#		verbose_name = 'Комментарий'
#		verbose_name_plural = 'Комментарии'

#	def __str__(self):
#		return self.comment_text[0:200]

#	def get_offser(self):
#		level = len(self.path) - 1
#		if level > 5:
#			level = 5
#		return level

#	def get_col(self):
#		level = len(self.path) - 1
#		if level > 5:
#			level = 5
#		return 12 - level
