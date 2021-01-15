from django.urls import path
# from .views import ArticleListView, ArticleDetailView
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.articles, name='articles-home'),
    # path('articles/', ArticleListView.as_view(), name='articles-home'),
    # path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),  # /article-details/<article_id>
    path('', views.desc, name='desc-page'),  # /about/
    #path('randfor/', views.randfor, name='randfor-page'),  # /randfor/
    #path('desc_proj/', views.desc, name='desc-page'),
    #path('nlp/', views.nlp, name='nlp-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
