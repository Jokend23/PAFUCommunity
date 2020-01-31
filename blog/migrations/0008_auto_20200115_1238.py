# Generated by Django 3.0 on 2020-01-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200115_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True, verbose_name='Адрес страницы')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Просмотр',
                'verbose_name_plural': 'Просмотры',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_score',
        ),
    ]