
from django.conf import settings
from django.conf.urls.static import static

from ads.views import views_ads
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ad/', include('ads.urls.urls_ads')),

    path('user/', include('ads.urls.urls_user')),

    path('cat/', include('ads.urls.urls_cat')),


    path('', views_ads.root),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
