from django.db import models
from db.base_model import BaseModel
from ckeditor.fields import RichTextField
# Create your models here.


class ArticleManage(BaseModel):
    '''文章内容'''
    COLUMN = (
        (0, '建站'),
        (1, '框架'),
        (2, '前端'),
        (3, '数据库'),
        (4, '趣谈'),
        (5, '生活')
    )
    title = models.CharField(max_length=128, verbose_name='标题')
    auther = models.CharField(max_length=20, verbose_name='作者')
    summary = models.CharField(max_length=256, verbose_name='文章简介')
    read_times = models.IntegerField(default=0, verbose_name='阅读量')
    sum_up = models.IntegerField(default=0, verbose_name='点赞数')
    column = models.SmallIntegerField(default=0, choices=COLUMN, verbose_name='栏目')
    content = RichTextField(verbose_name='文章主体内容')

    class Meta:
        db_table = 'article_manage'
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleCommentManage(BaseModel):
    '''文章评论父类'''
    article_id = models.ForeignKey('ArticleManage', verbose_name='文章id')
    pub_user = models.ForeignKey('user.User', verbose_name='评论用户')
    pub_cont = models.CharField(max_length=256, verbose_name='评论内容')

    class Meta:
        db_table = 'article_comment_manage'
        verbose_name = '文章评论父类'
        verbose_name_plural = verbose_name


class ArticleCommentManageSon(BaseModel):
    '''文章评论子类'''
    comment_id = models.ForeignKey('ArticleManage', verbose_name='父评论id')
    pub_user = models.ForeignKey('user.User', verbose_name='评论用户')
    pub_cont = models.CharField(max_length=256, verbose_name='回复内容')

    class Meta:
        db_table = 'article_comment_manage_son'
        verbose_name = '文章评论子类'
        verbose_name_plural = verbose_name


