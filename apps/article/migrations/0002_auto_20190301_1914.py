# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-03-01 11:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecommentmanageson',
            name='pub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
        migrations.AddField(
            model_name='articlecommentmanage',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleManage', verbose_name='文章id'),
        ),
        migrations.AddField(
            model_name='articlecommentmanage',
            name='pub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
    ]
