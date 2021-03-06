from django.shortcuts import render
from django.views.generic import View
from article.models import ArticleManage, ArticleCommentManage, ArticleCommentManageSon

# Create your views here.


class Article(View):
    def get(self, request):
        '''文章页'''
        article = ArticleManage.objects.all()
        hot = ArticleManage.objects.order_by('-read_times')[:5]
        return render(request, 'article.html', {'article': article, 'hot': hot})


class ArticleDetail(View):
    def get(self, request, num):
        article = ArticleManage.objects.get(id=num)
        article.read_times += 1
        article.save()
        hot = ArticleManage.objects.order_by('-read_times')[:5]
        return render(request, 'article_detail.html', {'article': article, 'hot': hot})



