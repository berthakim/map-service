from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import FoliumView

urlpatterns = [
    path('', views.folium_map, name='folium-map'),
    # path('', FoliumView.as_view(), name='folium-map'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
