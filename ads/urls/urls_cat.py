from ads.views import views_cat

from django.urls import path

from rest_framework import routers

from ads.views.views_cat import CategoryViewSet

router_category = routers.SimpleRouter()
router_category.register('cat', CategoryViewSet)
