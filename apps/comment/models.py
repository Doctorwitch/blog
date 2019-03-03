from django.db import models
from db.base_model import BaseModel

# Create your models here.


class CommentManage(BaseModel):
    '''博客评论管理父类'''
    user_id = models.ForeignKey('user.User', verbose_name='评论用户')
    sum_up = models.IntegerField(default=0, verbose_name='点赞数')

    class Meta:
        '''博客评论父类'''
        db_table = 'comment_manage'
        verbose_name = '博客评论父类'
        verbose_name_plural = verbose_name


class CommentManageSon(BaseModel):
    '''博客评论子类'''
    user_id = models.ForeignKey('user.User', verbose_name='回复用户')
    pub_cont = models.CharField(max_length=256, verbose_name='回复内容')

    class Meta:
        '''博客评论子类'''
        db_table = 'comment_manage_son'
        verbose_name = '博客评论子类'
        verbose_name_plural = verbose_name


