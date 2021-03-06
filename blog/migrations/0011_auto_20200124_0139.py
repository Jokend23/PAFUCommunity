# Generated by Django 3.0 on 2020-01-23 18:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Статистика Статьи',
                'verbose_name_plural': 'Статистики статей',
            },
        ),
        migrations.DeleteModel(
            name='PageHit',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_views',
        ),
        migrations.AddField(
            model_name='articlestatistic',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='Статья'),
        ),
    ]
