from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import ...

from django.http import HttpResponse
from django.views.generic import TemplateView


# def articles(request):  # main (home) page
#     context = {
#         'articles': Article.objects.all(),
#     }
#     return render(request, 'artic/articles.html', context)

# class ArticleListView(ListView):
#     model = Article
#     template_name = 'artic/articles.html'  # url:<app>/<model>_<viewtype>.html
#     context_object_name = 'articles'
#     ordering = ['-artic_date']

def flood(request):
    return render(request, 'flood/flood.html')
