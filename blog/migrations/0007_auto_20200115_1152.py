# Generated by Django 3.0 on 2020-01-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200112_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_score',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AddField(
            model_name='articletype',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Транслит'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_files',
            field=models.ManyToManyField(blank=True, to='blog.UploadedFile', verbose_name='Прикрепленный файлы'),
        ),
    ]
