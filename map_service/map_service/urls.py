"""map_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('descriptions.urls')),
    path('map_meteo/', include('meteo.urls')),
    path('map_flood/', include('flood.urls')),
    path('map_fire/', include('fire.urls')),
    path('weather/', include('weather.urls')),
    path('weather_map/', include('weather_map.urls')),
    path('folium/', include('folium_map.urls')),
    path('folium0/', include('folium_map0.urls')),
    path('health/', include('health.urls')),
    path('anim/', include('anim.urls')),
    path('foliums/', include('foliums.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
