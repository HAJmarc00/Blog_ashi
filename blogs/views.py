from django.shortcuts import render
from django.views.generic import TemplateView  
from .models import *

class IndexPage(TemplateView):
    template_name = "index.html"

    def get(self, request, **kwargs):

        article_data = []
        all_articles = Article.objects.all().order_by('created_at')[:12]
        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at,
            })

        promoted_data = []
        all_promoted_articles = Article.objects.filter(promote=True)
        for promoted_article in all_promoted_articles:
            promoted_data.append({
                'category': promoted_article.category.title,
                'title': promoted_article.title,
                'author': promoted_article.author.user.username,
                'avatar': promoted_article.author.avatar.url if promoted_article.author.avatar else None,
                'created_at': promoted_article.created_at,
            })

        context = {
            'articles': article_data,
            'promoted_articles_data': promoted_data,
        }

        return render(request, self.template_name, context)