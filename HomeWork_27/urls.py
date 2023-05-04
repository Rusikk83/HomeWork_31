
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from ads.urls.urls_selecion import router_selection
from ads.views import views_ads
from django.contrib import admin
from django.urls import path, include

from ads.views.views_location import LocationViewSet

router_location = routers.SimpleRouter()
router_location.register('location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ad/', include('ads.urls.urls_ads')),

    path('user/', include('ads.urls.urls_user')),

    path('cat/', include('ads.urls.urls_cat')),


    path('', views_ads.root),

]

urlpatterns += router_location.urls
urlpatterns += router_selection.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

