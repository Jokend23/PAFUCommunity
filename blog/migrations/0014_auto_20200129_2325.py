# Generated by Django 3.0 on 2020-01-29 16:25

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20200125_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('news_create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('news_published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('news_title', models.CharField(max_length=100, verbose_name='Название')),
                ('news_text_short', models.TextField(verbose_name='Краткое содержание')),
                ('news_text', models.TextField(verbose_name='Текст')),
                ('article_image', models.ImageField(upload_to=blog.models.rename_image, verbose_name='Изображение')),
                ('news_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]