from django.urls import path
# from .views import ArticleListView, ArticleDetailView
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.desc, name='desc-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
