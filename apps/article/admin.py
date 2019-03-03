from django.contrib import admin
from article.models import ArticleManage, ArticleCommentManage, ArticleCommentManageSon

# Register your models here.
admin.site.register(ArticleManage)
admin.site.register(ArticleCommentManage)
admin.site.register(ArticleCommentManageSon)
